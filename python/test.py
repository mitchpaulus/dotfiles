import unittest
import psychrometrics

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

if __name__ == "__main__":
    unittest.main()
