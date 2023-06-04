# pylint: disable=missing-final-newline
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=unused-import
# pylint: disable=ungrouped-imports
from Exceptions.LoggedDecorator import LoggedDecorator
from Managers.SM import SM
from Models.RM import RM
from Models.chainsaw import Chainsaw
from Models.electric_saw import ElectricSaw
from Exceptions import RedundantBatteryException, RedundantFuelException

if __name__ == '__main__':
    regular_manager = RM()
    chainsaw1 = Chainsaw("Stihl", 1200, 120, 16, 500)
    chainsaw2 = Chainsaw("Husqvarna", 1500, 180, 18, 600)
    electric_saw1 = ElectricSaw("Bosch", 1000, 90, "Brushless", 400, regular_manager)
    electric_saw2 = ElectricSaw("Makita", 800, 120, "Brushed", 300, regular_manager)

    regular_manager.add_saw(chainsaw1)
    regular_manager.add_saw(chainsaw2)
    regular_manager.add_saw(electric_saw1)
    regular_manager.add_saw(electric_saw2)

    @LoggedDecorator(RedundantBatteryException, "console")
    def charge_saw(saw):
        if isinstance(saw, ElectricSaw):
            if saw.battery_capacity == 100:
                raise RedundantBatteryException("Battery is already fully charged.")
            else:
                saw.battery_capacity += 10
                print(f"Charged {saw.brand} electric saw. Battery capacity: {saw.battery_capacity}%")


    @LoggedDecorator(RedundantFuelException, "file")
    def refuel_saw(saw):
        if isinstance(saw, Chainsaw):
            if saw.fuel_capacity == 100:
                raise RedundantFuelException("Fuel tank is already full.")
            else:
                saw.fuel_capacity += 10
                print(f"Refueled {saw.brand} chainsaw. Fuel capacity: {saw.fuel_capacity}%")

    print("Regular Manager:")
    for saw in regular_manager:
        print(saw)

    print("\nCharging electric saws...")
    for saw in regular_manager:
        if isinstance(saw, ElectricSaw):
            try:
                charge_saw(saw)
            except RedundantBatteryException as e:
                print(f"RedundantBatteryException: {e}")

    print("\nRefueling chainsaws...")
    for saw in regular_manager:
        if isinstance(saw, Chainsaw):
            try:
                refuel_saw(saw)
            except RedundantFuelException as e:
                print(f"RedundantFuelException: {e}")

    print("\nUpdated Electric Saws:")
    for saw in regular_manager:
        if isinstance(saw, ElectricSaw):
            print(saw)

    print("\nUpdated Chainsaws:")
    for saw in regular_manager:
        if isinstance(saw, Chainsaw):
            print(saw)


