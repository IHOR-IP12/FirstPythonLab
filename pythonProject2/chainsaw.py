from saw import Saw


class Chainsaw(Saw):
    def __init__(self, brand, power, engine_work_duration, fuel_tank_capacity, fuel_level, is_working=False):
        super().__init__(brand, power, engine_work_duration, is_working)
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_level = fuel_level

    def start(self):
        self.is_working = True

    def stop(self):
        self.is_working = False

    def cut_wood(self, length):
        fuel_needed = length / 10
        self.fuel_level = 0 if fuel_needed > self.fuel_level else self.fuel_level - fuel_needed
        self.is_working = self.fuel_level != 0

    def get_remaining_work_time(self):
        return self.fuel_level / (self.fuel_tank_capacity / self.engine_work_duration)
