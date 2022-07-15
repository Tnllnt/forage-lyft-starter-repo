from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        total_wear = 0
        for i in self.tires_wear:
            total_wear = total_wear + i
        return total_wear >= 3
