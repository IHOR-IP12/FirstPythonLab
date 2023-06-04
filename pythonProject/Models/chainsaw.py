# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=bad-option-value
# pylint: disable=too-few-public-methods
# pylint: disable=missing-final-newline
# pylint: disable=too-many-arguments
# pylint: disable=line-too-long
# pylint: disable=import-error
# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from Exceptions.LoggedDecorator import LoggedDecorator
from Exceptions.RedundantFuelException import RedundantFuelException
from Models.saw import Saw


class Chainsaw(Saw):
    def __init__(self, brand, power, engine_work_duration, bar_length, fuel_capacity):
        self.brand = brand
        self.power = power
        self.engine_work_duration = engine_work_duration
        self.bar_length = bar_length
        self.fuel_capacity = fuel_capacity

    def get_remaining_work_time(self):
        remaining_time = self.engine_work_duration / (self.power / 100)
        return remaining_time

    def __str__(self):
        return f"Chainsaw - Brand: {self.brand}, Power: {self.power}, Engine Work Duration: {self.engine_work_duration} minutes, Bar Length: {self.bar_length}, Fuel Capacity: {self.fuel_capacity}, Remaining Work Time: {self.get_remaining_work_time()} hours"

        @LoggedDecorator(RedundantFuelException, "console")
        def do_something(self):
            if self.fuel_capacity == 100:
                raise RedundantFuelException()
            return "Doing something..."