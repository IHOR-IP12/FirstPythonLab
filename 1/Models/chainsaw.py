# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=bad-option-value
# pylint: disable=too-few-public-methods
# pylint: disable=missing-final-newline
# pylint: disable=too-many-arguments
# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from saw import Saw


class Chainsaw(Saw):
    def __init__(self, brand, power, engine_work_duration, fuel_tank_capacity, fuel_level):
        super().__init__(brand, power, engine_work_duration)
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_level = fuel_level

    def start(self):
        self.is_working = True

    def stop(self):
        self.is_working = False

    def cut_wood(self, length):
        fuel_needed = length / 10
        self.fuel_level = max(0, self.fuel_level - fuel_needed)
        self.is_working = self.fuel_level > 0

    def get_remaining_work_time(self) -> float:
        return self.fuel_level / (self.fuel_tank_capacity / self.engine_work_duration)

    def do_something(self) -> str:
        return "Chainsaw: Doing something"