import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_service(self):
        Component = WilloughbyEngine(31001, 1000)
        self.assertFalse(Component.needs_service())
    
    def test_service_broke(self):
        Component = WilloughbyEngine(61001, 1000)
        self.assertTrue(Component.needs_service())

if __name__ == '__main__':
    unittest.main()
