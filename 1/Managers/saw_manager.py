# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=R0903
# pylint: disable=C0304
class SawManager:
    def __init__(self):
        self.saw_list = []

    def add_saw(self, saw):
        self.saw_list.append(saw)

    def __len__(self) -> int:
        return len(self.saw_list)

    def __getitem__(self, index: int):
        return self.saw_list[index]

    def __iter__(self):
        return iter(self.saw_list)

    def execute_do_something(self):
        return [s.do_something() for s in self.saw_list]

    def get_enumerated_objects(self):
        return [(i, obj) for i, obj in enumerate(self.saw_list)]

    def get_zip_result(self):
        return zip(self.saw_list, self.execute_do_something())

    def get_attribute_values_by_type(self, data_type) -> dict:
        return {attr: value for attr, value in self.__dict__.items() if isinstance(value, data_type)}

    def check_condition_all_any(self, condition):
        return {
            "all": all(condition(obj) for obj in self.saw_list),
            "any": any(condition(obj) for obj in self.saw_list)
        }

