import unittest
from battery.spindler_battery import SpindlerBattery
from datetime import datetime

today = datetime.today().date()

class TestNubbinBattery(unittest.TestCase):
    def test_service(self):
        Component = SpindlerBattery(today, today.replace(year=today.year-1))
        self.assertFalse(Component.needs_service())
    
    def test_service_broke(self):
        Component = SpindlerBattery(today, today.replace(year=today.year-4))
        self.assertTrue(Component.needs_service())

if __name__ == '__main__':
    unittest.main()
