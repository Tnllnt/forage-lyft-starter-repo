from abc import ABC
from battery.battery import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date.year - self.last_service_date.year >= 4