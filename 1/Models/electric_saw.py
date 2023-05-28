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


class ElectricSaw(Saw):
    def __init__(self, brand, power, engine_work_duration, motor_type, battery_capacity):
        super().__init__(brand, power, engine_work_duration)
        self.motor_type = motor_type
        self.battery_capacity = battery_capacity

    def get_remaining_work_time(self) -> float:
        return self.battery_capacity / (self.power / self.engine_work_duration)

    def do_something(self) -> str:
        return "Electric Saw: Doing something"