from saw import Saw


class ElectricSaw(Saw):
    def __init__(self, brand, power, engine_work_duration, motor_type, battery_capacity, is_working=False):
        super().__init__(brand, power, engine_work_duration, is_working)
        self.motor_type = motor_type
        self.battery_capacity = battery_capacity

    def get_remaining_work_time(self):
        return self.battery_capacity / (self.power / self.engine_work_duration)
