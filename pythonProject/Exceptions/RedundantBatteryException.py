
class RedundantBatteryException(Exception):
    def __init__(self):
        super().__init__("Battery capacity is already at 100%")
