from abc import ABC, abstractmethod


class Saw(ABC):
    def __init__(self, brand, power, engine_work_duration, is_working=False):
        self.brand = brand
        self.power = power
        self.engine_work_duration = engine_work_duration
        self.is_working = is_working

    @abstractmethod
    def get_remaining_work_time(self):
        pass