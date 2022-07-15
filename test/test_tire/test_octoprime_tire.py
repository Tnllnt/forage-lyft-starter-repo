import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_service(self):
        tires_wear = [0,0,0,0]
        tire = OctoprimeTire(tires_wear)
        self.assertFalse(tire.needs_service())
    
    def test_service_broke(self):
        tires_wear = [1,0,1,1]
        tire = OctoprimeTire(tires_wear)
        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
