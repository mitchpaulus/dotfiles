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
