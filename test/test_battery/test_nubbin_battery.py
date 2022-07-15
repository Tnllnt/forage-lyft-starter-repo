import unittest
from battery.nubbin_battery import NubbinBattery
from datetime import datetime

today = datetime.today().date()

class TestNubbinBattery(unittest.TestCase):
    def test_service(self):
        Component = NubbinBattery(today, today.replace(year=today.year-1))
        self.assertFalse(Component.needs_service())
    
    def test_service_broke(self):
        Component = NubbinBattery(today, today.replace(year=today.year-5))
        self.assertTrue(Component.needs_service())

if __name__ == '__main__':
    unittest.main()
