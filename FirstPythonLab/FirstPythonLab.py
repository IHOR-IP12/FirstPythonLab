class Chainsaw:
    def __init__(self, brand, power, fuelTankCapacity):
        self.brand = brand
        self.power = power
        self.fuelTankCapacity = fuelTankCapacity
        self.fuelLevel = 0.0
        self.isWorking = False

    def start(self):
        self.isWorking = True

    def stop(self):
        self.isWorking = False

    def cutWood(self, length):
        fuelConsumption = length * 0.1  # Розрахунок споживання палива (100 мл на 1 м)
        if self.fuelLevel >= fuelConsumption:
            self.fuelLevel -= fuelConsumption
        else:
            self.fuelLevel = 0.0
            self.isWorking = False