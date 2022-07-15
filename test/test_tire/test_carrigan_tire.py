import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_service(self):
        tires_wear = [0,0,0,0]
        tire = CarriganTire(tires_wear)
        self.assertFalse(tire.needs_service())
    
    def test_service_broke(self):
        tires_wear = [0,0.9,0,0]
        tire = CarriganTire(tires_wear)
        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
