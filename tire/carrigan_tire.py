from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        for i in self.tires_wear:
            if i >= 0.9:
                return True
        return False
