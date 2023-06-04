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
from Exceptions.RedundantBatteryException import RedundantBatteryException
from Models.saw import Saw


class ElectricSaw(Saw):
    def __init__(self, brand, power, engine_work_duration, motor_type, battery_capacity, manager):
        super().__init__(brand, power, engine_work_duration)
        self.motor_type = motor_type
        self.battery_capacity = battery_capacity
        self.manager = manager

    def get_remaining_work_time(self):
        return self.battery_capacity / (self.power / self.engine_work_duration)

    def __str__(self):
        return f"Electric Saw - Brand: {self.brand}, Power: {self.power}, Engine Work Duration: {self.engine_work_duration} minutes, Motor Type: {self.motor_type}, Battery Capacity: {self.battery_capacity}, Remaining Work Time: {self.get_remaining_work_time()} hours"

    def do_something(self): # Він містить усі атрибути об'єкта та їхні значення.
        other_obj = self.manager[0]
        return other_obj

    @LoggedDecorator(RedundantBatteryException, "file")
    def do_something(self):
        if self.battery_capacity == 100:
            raise RedundantBatteryException()
        return "Doing something..."