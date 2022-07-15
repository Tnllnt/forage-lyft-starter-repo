import unittest
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_service(self):
        Component = CapuletEngine(0, 1000)
        self.assertFalse(Component.needs_service())
    
    def test_service_broke(self):
        Component = CapuletEngine(31001, 1000)
        self.assertTrue(Component.needs_service())

if __name__ == '__main__':
    unittest.main()
