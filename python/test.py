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

    def test_specific_volume(self):
        tdb = 60
        w = 0.01
        specific_volume = psychrometrics.specific_volume_from_toa_w(tdb, w)
        self.assertAlmostEqual(specific_volume, 13.31151850962418, delta=0.01)



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

if __name__ == "__main__":
    unittest.main()
