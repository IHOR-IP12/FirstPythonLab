from chainsaw import Chainsaw
from electric_saw import ElectricSaw
from saw_manager import SawManager
from electric_saw import ElectricSaw
from chainsaw_manager import ChainsawManager
from electric_saw_manager import ElectricSawManager


chainsaw_manager = ChainsawManager()
chainsaw_manager.add_saw(Chainsaw("Stihl", 2000, 500, 500, 250))
chainsaw_manager.add_saw(Chainsaw("Husqvarna", 1800, 400, 400, 150))
chainsaw_manager.add_saw(Chainsaw("Makita", 2200, 550, 600, 300))
chainsaw_manager.add_saw(Chainsaw("Echo", 1600, 350, 300, 100))
chainsaw_manager.add_saw(Chainsaw("Black & Decker", 1200, 250, 200, 50))

electric_saw_manager = ElectricSawManager()
electric_saw_manager.add_saw(ElectricSaw("Bosch", 2000, 600, "Brushless", 1000))
electric_saw_manager.add_saw(ElectricSaw("Dewalt", 1800, 550, "Brushless", 800))
electric_saw_manager.add_saw(ElectricSaw("Makita", 2200, 700, "Brushed", 1200))
electric_saw_manager.add_saw(ElectricSaw("Ryobi", 1500, 400, "Brushless", 600))
electric_saw_manager.add_saw(ElectricSaw("Milwaukee", 1700, 500, "Brushed", 900))

print("All chainsaws:")
for saw in chainsaw_manager.saw_list:
    print(saw)

print("\nAll electric saws:")
for saw in electric_saw_manager.saw_list:
    print(saw)

print("\nChainsaws with power greater than 1800W:")
for saw in chainsaw_manager.find_all_with_power_greater_than(1800):
    print(saw)

print("\nElectric saws with remaining work time greater than 5 hours:")
for saw in electric_saw_manager.find_all_with_remaining_work_time_greater_than(5):
    print(saw)

print("\nChainsaws made by Makita:")
for saw in chainsaw_manager.find_all_with_brand("Makita"):
    print(saw)

print("\nElectric saws made by Bosch:")
for saw in electric_saw_manager.find_all_with_brand("Bosch"):
    print(saw)
