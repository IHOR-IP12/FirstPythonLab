# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=bad-option-value
# pylint: disable=too-few-public-methods
# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=missing-final-newline
from abc import ABC, abstractmethod


from abc import ABC, abstractmethod


class Saw(ABC):
    def __init__(self, brand, power, engine_work_duration, is_working=False):
        self.brand = brand
        self.power = power
        self.engine_work_duration = engine_work_duration
        self.is_working = is_working

    @abstractmethod
    def get_remaining_work_time(self) -> float:
        pass

    @abstractmethod
    def do_something(self) -> str:
        pass

