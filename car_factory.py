import imp
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


#Create new car models with established classes
class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tires_wear)
        calliope = Car(engine, battery, tire)
        return calliope
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tires_wear)
        glissade = Car(engine, battery, tire)
        return glissade
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tires_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTire(tires_wear)
        palindrome = Car(engine, battery, tire)
        return palindrome
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tires_wear)
        rorschach = Car(engine, battery, tire)
        return rorschach
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tires_wear)
        thovex = Car(engine, battery, tire)
        return thovex