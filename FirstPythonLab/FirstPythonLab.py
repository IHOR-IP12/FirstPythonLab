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
        fuelConsumption = length * 0.1  
        if self.fuelLevel >= fuelConsumption:
            self.fuelLevel -= fuelConsumption
        else:
            self.fuelLevel = 0.0
            self.isWorking = False
