from saw_manager import SawManager


class ElectricSawManager(SawManager):
    def find_all_with_brand(self, brand):
        return [s for s in self.saw_list if s.brand == brand]

    def find_all_with_remaining_work_time_greater_than(self, remaining_work_time):
        return [s for s in self.saw_list if s.get_remaining_work_time() > remaining_work_time]