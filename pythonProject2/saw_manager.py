class SawManager:
    def __init__(self):
        self.saw_list = []

    def add_saw(self, saw):
        self.saw_list.append(saw)

    def find_all_with_power_greater_than(self, power):
        return [s for s in self.saw_list if s.power > power]


