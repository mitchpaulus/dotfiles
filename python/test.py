import unittest
import psychrometrics
import mputils

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

if __name__ == "__main__":
    unittest.main()
