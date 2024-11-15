import unittest
import psychrometrics
import mputils
import re

def sorted_nicely( l ):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

class TestPsychrometrics(unittest.TestCase):
    def test_sat_pressure(self):
        temp = 60 # °F
        saturation_pressure = psychrometrics.sat_partial_pressure(temp)
        self.assertAlmostEqual(saturation_pressure, 0.25638, delta=0.1)

    def test_sat_pressure_si(self):
        test_cases = [
            (-60, 0.00108),
            (-10, 0.25987),
            (0, 0.61121),
            (10, 1.2282),
            (150, 476.10),
        ]

        for case in test_cases:
            saturation_pressure_kPa = psychrometrics.sat_partial_pressure_si(case[0])

            # match within 0.01% of tabular value or 0.0001 absolute, whichever greater
            delta = max(case[1] * 0.0001, 0.0001)

            self.assertAlmostEqual(saturation_pressure_kPa, case[1], delta=delta)


    def test_specific_volume(self):
        tdb = 60
        w = 0.01
        specific_volume = psychrometrics.specific_volume_from_toa_w(tdb, w)
        self.assertAlmostEqual(specific_volume, 13.31151850962418, delta=0.01)


    def test_wet_bulb(self):
        tdb = 90
        w = 0.014

        twb = psychrometrics.twb_from_tdb_w(tdb, w)
        print(twb)
        self.assertAlmostEqual(twb, 73.5, delta=0.1)


class TestSorting(unittest.TestCase):
    def test_version_sort_by(self):
        class TestClass:
            def __init__(self, prop1, prop2):
                self.prop1 = prop1
                self.prop2 = prop2

            def __str__(self):
                return f'TestObj: {self.prop1} {self.prop2}'

            def __repr__(self):
                return f'TestObj: {self.prop1} {self.prop2}'

        test_list = [TestClass(1, 2), TestClass(20, 3), TestClass(3, 4)]

        test_list = mputils.version_sort_by(test_list, lambda x: str(x.prop1))

        self.assertEqual(test_list[0].prop1, 1)
        self.assertEqual(test_list[1].prop1, 3)
        self.assertEqual(test_list[2].prop1, 20)

    def test_version_sort_in_place(self):
        test_list = ["1", "20", "3"]
        mputils.version_sort_in_place(test_list)

        self.assertEqual(test_list[0], "1")
        self.assertEqual(test_list[1], "3")
        self.assertEqual(test_list[2], "20")

    def test_version_sort_mix(self):
        test_list = ["1a", "a1"]
        mputils.version_sort_in_place(test_list)


    def test_version_sort_stack_overflow(self):
        s = set(['booklet', '4 sheets', '48 sheets', '12 sheets'])
        for x in sorted_nicely(s):
            print(x)
        for x in mputils.version_sort(s):
            print(x)


class TestPathResolve(unittest.TestCase):
    def test_path_resolve(self):
        path = mputils.resolve_path('../../test.py', '/mnt/c/Users/mpaulus/')
        self.assertEqual(path, '/mnt/c/test.py')


class TestFindDevice(unittest.TestCase):
    def test_1(self):
        test = '/CEC_AHU-2/BACnet Interface/IP Network/VAV_2_1/Application/Values/RmTmp/Value'
        device = mputils.device_from_path(test)
        self.assertEqual(device, 'VAV_2_1')


class TestItp(unittest.TestCase):
    def test_wikipedia(self):
        def f(x):
            return x**3 - x - 2

        zero, zero_val, iterations = mputils.itp(1, 2, f, 10**(-20), True)
        print(zero, zero_val, iterations)
        self.assertAlmostEqual(zero, 1.52138, 4)

class TestMinIndex(unittest.TestCase):
    def test_minindex(self):
        test_list = [1, -1, 3, 5]
        idx, value = mputils.min_index(test_list)
        self.assertEqual(idx, 1)
        self.assertEqual(value, -1)

class TestDates(unittest.TestCase):
    def test_rd_dates(self):
        test_data = [
            (-214193, -586, 7, 24),
            (-61387, -168, 12, 5),
            (25469, 70, 9, 24),
            (49217, 135, 10, 2),
            (171307, 470, 1, 8),
            (210155, 576, 5, 20),
            (253427, 694, 11, 10),
            (369740, 1013, 4, 25),
            (400085, 1096, 5, 24),
            (434355, 1190, 3, 23),
            (452605, 1240, 3, 10),
            (470160, 1288, 4, 2),
            (473837, 1298, 4, 27),
            (507850, 1391, 6, 12),
            (524156, 1436, 2, 3),
            (544676, 1492, 4, 9),
            (567118, 1553, 9, 19),
            (569477, 1560, 3, 5),
            (601716, 1648, 6, 10),
            (613424, 1680, 6, 30),
            (626596, 1716, 7, 24),
            (645554, 1768, 6, 19),
            (664224, 1819, 8, 2),
            (671401, 1839, 3, 27),
            (694799, 1903, 4, 19),
            (704424, 1929, 8, 25),
            (708842, 1941, 9, 29),
            (709409, 1943, 4, 19),
            (709580, 1943, 10, 7),
            (727274, 1992, 3, 17),
            (728714, 1996, 2, 25),
            (744313, 2038, 11, 10),
            (764652, 2094, 7, 18),
        ]

        for rd, year, month, day in test_data:
            self.assertEqual(mputils.fixed_from_gregorian(year, month, day), rd)

            y, m, d = mputils.ymd_from_rd(rd)
            self.assertEqual(y, year)
            self.assertEqual(m, month)
            self.assertEqual(d, day)

class TestPolyFit(unittest.TestCase):
    def test_poly_fit(self):
        # Test case from page 458 of "Numerical Methods for Engineers" by Steven C. Chapra
        x = [0.0, 1, 2, 3, 4, 5]
        y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]

        a0, a1, a2 = mputils.poly_fit(x, y)
        print(a0, a1, a2)

        self.assertAlmostEqual(a0, 2.47857, 4)
        self.assertAlmostEqual(a1, 2.35929, 3)
        self.assertAlmostEqual(a2, 1.86071, 3)

class TestDateTimeParsing(unittest.TestCase):
    def test_parse_date_1(self):
        date_str = '8/27/2024 5:05:19 PM'
        date_parts = mputils.parse_datetime(date_str)
        self.assertEqual(date_parts, [2024, 8, 27, 17, 5, 19])

    def test_parse_date_2(self):
        date_str = '2024/8/7 12:05 AM'
        date_parts = mputils.parse_datetime(date_str)
        self.assertEqual(date_parts, [2024, 8, 7, 0, 5])

    def test_parse_date_3(self):
        date_str = '2024-8-7 12:05 PM'
        date_parts = mputils.parse_datetime(date_str)
        self.assertEqual(date_parts, [2024, 8, 7, 12, 5])

class TestDateTimeParsing2(unittest.TestCase):
    def test_parse_date_1(self):
        date_str = '8/27/2024 5:05:19 PM'
        date_lexer = mputils.DateLexer(date_str)
        date_parts = date_lexer.tokenize()
        self.assertEqual(date_parts, ['8', '27', '2024', '5', '05', '19', 'PM'])

    def test_parse_date_2(self):
        date_str = '8/27/2024 5:05:19 P.M.'
        date_lexer = mputils.DateLexer(date_str)
        date_parts = date_lexer.tokenize()
        self.assertEqual(date_parts, ['8', '27', '2024', '5', '05', '19', 'P', 'M'])

if __name__ == "__main__":
    unittest.main()
