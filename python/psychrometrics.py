import math

def specific_volume_from_toa_w(t_oa: float, w: float, pressure: float = 14.696):
    """
    :param t_oa: Outside air temperature [°F]
    :param w: Humidity Ratio
    :param pressure: Pressure [psia]
    :return: Specific Volume [ft³/lb]
    """
    return 0.370486*(t_oa + 459.67) * (1 + 1.607858*(w))/(pressure)

def specific_volume_from_toa_twb(t_oa: float, t_wb: float, total_pressure: float = 14.696):
    """
    :param t_oa: Outside air temperature [°F]
    :param t_wb: Wet bulb temperature [°F]
    :return: Specific Volume [ft³/lb]
    """
    return 0.370486*(t_oa + 459.67) * (1 + 1.607858*(w_from_toa_twb(t_oa, t_wb, total_pressure))) / total_pressure

def air_density_from_toa_w(t_oa: float, w: float, pressure: float = 14.696):
    """
    :param t_oa: Outside air temperature [°F]
    :param w: Humidity Ratio
    :param pressure: Pressure [psia]
    :return: Air Density [lb/ft³]
    """
    return 1 / specific_volume_from_toa_w(t_oa, w, pressure)

def air_density_from_toa_twb(t_oa: float, t_wb: float, total_pressure: float = 14.696) -> float:
    """
    :param t_oa: Outside air temperature [°F]
    :param t_wb: Wet bulb temperature [°F]
    :param total_pressure: Pressure [psia]
    :return: Air Density [lb/ft³]
    """
    return 1 / specific_volume_from_toa_twb(t_oa, t_wb, total_pressure)

def absolute_temp(t: float):
    return t + 459.67

def sat_partial_pressure(t: float) -> float:
    """Saturated Water Vapor Partial Pressure in psi from temperature in °F"""

    if t > 150:
        raise ValueError("Temperature must be less than 150°F")

    abs_temp = absolute_temp(t)
    if abs_temp > 491.67:
        return math.exp(-1.0440397e4/abs_temp +
                -1.129465e1 +
                -2.7022355e-2*abs_temp +
                1.289036e-5*abs_temp*abs_temp +
                -2.4780681e-9*abs_temp*abs_temp*abs_temp +
                6.5459673*math.log(abs_temp))
    else:
        return math.exp(-1.0214165e4/abs_temp +
                   -4.8932428 +
                   -5.376579e-3*abs_temp +
                   1.9202377e-7*abs_temp*abs_temp +
                   3.5575832e-10*abs_temp*abs_temp*abs_temp +
                   -9.0344688e-14*abs_temp*abs_temp*abs_temp*abs_temp +
                   4.1635019*math.log(abs_temp))


def sat_partial_pressure_si(t: float) -> float:
    t_kelvin = t + 273.15

    if t >= 0:
        n1  = 0.11670521452767e4
        n2  = -0.72421316703206e6
        n3  = -0.17073846940092e2
        n4  = 0.12020824702470e5
        n5  = -0.32325550322333e7
        n6  = 0.14915108613530e2
        n7  = -0.48232657361591e4
        n8  = 0.40511340542057e6
        n9  = -0.23855557567849e0
        n10 = 0.65017534844798e3

        theta = t_kelvin + n9 / (t_kelvin - n10)

        A = theta*theta + n1 * theta + n2
        B = n3 * theta * theta + n4 * theta + n5
        C = n6 * theta * theta + n7 * theta + n8

        pws = 1000 * ((2 * C) / ( -B + math.sqrt(B*B - 4*A*C) ))**4
    else:
        a1 = -0.212144006e2
        a2 = 0.273203819e2
        a3 = -0.610598130e1
        b1 = 0.333333333e-2
        b2 = 0.120666667e1
        b3 = 0.170333333e1
        theta = t_kelvin / 273.16

        pws = 0.611657 * math.exp((1 / theta) * (a1*theta**b1 +  a2*theta**b2 + a3*theta**b3)  )

    return pws

def w_from_partial_pressure(pv: float, total_pressure: float = 14.696) -> float:
    return 0.621945 * pv / (total_pressure - pv)

def w_from_toa_twb(t_oa: float, t_wb: float, total_pressure: float = 14.696) -> float:
    """
    :param t_oa: Outside air temperature [°F]
    :param t_wb: Wet bulb temperature [°F]
    :return: Humidity Ratio
    """
    sat_partial_press_at_wet_bulb = sat_partial_pressure(t_wb)
    w_star = w_from_partial_pressure(sat_partial_press_at_wet_bulb, total_pressure)

    if t_wb > 32:
        return ((1093 - 0.556*(t_wb))*(w_star) - 0.24*((t_oa) - (t_wb))) / (1093 + 0.444*(t_oa) - (t_wb))
    else:
        return ((1220 - 0.04*(t_wb))*(w_star) - 0.24*((t_oa) - (t_wb))) / (1220 + 0.444*(t_oa) - 0.48*(t_wb))


def h_sat(t: float) -> float:
    """
    :param t: Temperature [°F]
    :return: Enthalpy [Btu/lb]
    """
    p_sat = sat_partial_pressure(t)
    w_sat = w_from_partial_pressure(p_sat)
    return 0.24*t + w_sat*(1061 + 0.444*t)

def h_from_tdb_w(tdb: float, w: float) -> float:
    return 0.24*tdb + w*(1061 + 0.444*tdb)


def w_from_tdb_rh(tdb: float, rh: float) -> float:
    """
    :param tdb: Dry bulb temperature [°F]
    :param rh: Relative Humidity [%] (0-100)
    :return: Humidity Ratio
    """

    pv = rh/100 * sat_partial_pressure(tdb)
    return w_from_partial_pressure(pv)



def zero_function(twb: float, tdb: float, w: float) -> float:
    w_star = w_from_partial_pressure(sat_partial_pressure(twb))

    numerator = (1093 - 0.556 * twb)* w_star - 0.24 * (tdb - twb)
    denom = 1093 + 0.444 * tdb - twb

    return numerator / denom - w


def deriv_zero_function(twb: float, tdb: float) -> float:
    p_sat_twb = sat_partial_pressure(twb)

    # Using tetens for derivative
    d_psat_d_twb = 0.088586 * math.exp((1727*twb -55264) / (100 * twb + 39514)) * 73767078 / ( (100 * twb + 39514)**2 )

    d_w_star_d_twb = 0.621945 * ((14.696 - p_sat_twb)*d_psat_d_twb + p_sat_twb * d_psat_d_twb) / ((14.696 - p_sat_twb)**2)

    w_star = w_from_partial_pressure(p_sat_twb)
    n = (1093 - 0.556*twb) * w_star - 0.24 * (tdb - twb)
    d = 1093+0.444*tdb - twb

    dn = (1093-0.556*twb) * d_w_star_d_twb - 0.556 * w_star + 0.24
    dd = -1

    return (d*dn - n*dd) / (d*d)


def twb_from_tdb_w(tdb: float, w: float) -> float:
    """Return wet bulb temperature [°F] given dry bulb temperature [°F] and humidity ratio"""
    initial_guess = tdb - 5

    z = 10
    tries = 0

    while z > 0.000001 and tries < 20:
        z = zero_function(initial_guess, tdb, w)
        dz = deriv_zero_function(initial_guess, tdb)
        initial_guess = initial_guess - z/dz
        tries += 1

    return initial_guess
