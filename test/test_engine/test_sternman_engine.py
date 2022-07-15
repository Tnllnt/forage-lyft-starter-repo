import unittest
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_service(self):
        Component = SternmanEngine(False)
        self.assertFalse(Component.needs_service())
    
    def test_service_broke(self):
        Component = SternmanEngine(True)
        self.assertTrue(Component.needs_service())

if __name__ == '__main__':
    unittest.main()
