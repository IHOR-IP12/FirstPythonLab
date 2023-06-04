
class RedundantFuelException(Exception):
    def __init__(self, message="Redundant fuel detected"):
        super().__init__(message)
