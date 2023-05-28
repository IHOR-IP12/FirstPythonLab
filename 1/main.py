# pylint: disable=missing-final-newline
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
from Managers.saw_manager import SawManager
from Models.chainsaw import Chainsaw
from Models.electric_saw import ElectricSaw

saw_manager = SawManager()

chainsaw1 = Chainsaw("Makita", 2200, 60, 2.5, 1.8)
chainsaw2 = Chainsaw("STIHL", 1800, 45, 2.0, 1.2)
electric_saw1 = ElectricSaw("Bosch", 1500, 120, "Brushless", 5.0)

saw_manager.add_saw(chainsaw1)
saw_manager.add_saw(chainsaw2)
saw_manager.add_saw(electric_saw1)

print("All saws:")
for saw in saw_manager.saw_list:
    print(saw)

print("\nSaws with power greater than 1800W:")
power_threshold = 1800
for saw in saw_manager.find_all_with_power_greater_than(power_threshold):
    print(saw)

print("\nSaws made by Makita:")
brand = "Makita"
for saw in saw_manager.find_all_with_brand(brand):
    print(saw)

print("\nSaws with remaining work time greater than 5 hours:")
work_time_threshold = 5
for saw in saw_manager.find_all_with_remaining_work_time_greater_than(work_time_threshold):
    print(saw)