from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery): #initialize, works like a function w/ parameters
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()  #calls on respective functions
