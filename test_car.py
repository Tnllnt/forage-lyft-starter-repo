import unittest
from car_factory import CarFactory
from datetime import datetime

today = datetime.today().date()

class TestCars(unittest.TestCase):
    def test_service_cali(self):                        #return false
        Car = CarFactory.create_calliope(today, today.replace(year=today.year-1), 0, 1000)
        self.assertFalse(Car.needs_service())
    
    def test_service_cali_broke_battery(self):          #return true
        Car = CarFactory.create_calliope(today, today.replace(year=today.year-3), 0, 1000)
        self.assertTrue(Car.needs_service())
    
    def test_service_cali_broke_engine(self):           #return true
        Car = CarFactory.create_calliope(today, today.replace(year=today.year-1), 31001, 1000)
        self.assertTrue(Car.needs_service())

    def test_service_cali_broke_both(self):             #return true
        Car = CarFactory.create_calliope(today, today.replace(year=today.year-3), 31001, 1000)
        self.assertTrue(Car.needs_service())

    def test_service_glis(self):                        #return false
        Car = CarFactory.create_glissade(today, today.replace(year=today.year-1), 0, 1000)
        self.assertFalse(Car.needs_service())

    def test_service_pali(self):                        #return false
        Car = CarFactory.create_palindrome(today, today.replace(year=today.year-1), False)
        self.assertFalse(Car.needs_service())
    
    def test_service_pali_broke_engine(self):           #return true
        Car = CarFactory.create_palindrome(today, today.replace(year=today.year-1), True)
        self.assertTrue(Car.needs_service())

    def test_service_rors(self):                        #return false
        Car = CarFactory.create_rorschach(today, today.replace(year=today.year-3), 31001, 1000)
        self.assertFalse(Car.needs_service())
    
    def test_service_rors_broke_engine(self):           #return true
        Car = CarFactory.create_rorschach(today, today.replace(year=today.year-3), 61001, 1000)
        self.assertTrue(Car.needs_service())
    
    def test_service_rors_broke_battery(self):          #return true
        Car = CarFactory.create_rorschach(today, today.replace(year=today.year-5), 31001, 1000)
        self.assertTrue(Car.needs_service())
    
    def test_service_thov(self):                        #return false
        Car = CarFactory.create_thovex(today, today.replace(year=today.year-1), 0, 1000)
        self.assertFalse(Car.needs_service())


if __name__ == '__main__':
    unittest.main()
