# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=trailing-newlines
# pylint: disable=unnecessary-comprehension
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

    def __len__(self):
        # Перевизначений метод, який повертає кількість об'єктів пилок в
        return len(self.saw_list)

    def __getitem__(self, index):
        #: Перевизначений метод, який дозволяє отримувати об'єкти пилок за індексом.
        return self.saw_list[index]

    def __iter__(self):
        #: Перевизначений метод, який дозволяє ітерувати через об'єкти пилок в
        return iter(self.saw_list)

    def find_all_with_power_greater_than(self, power_threshold):
        # Повертає список пилок, потужність яких більша за заданий поріг.
        result = []
        for saw in self.saw_list:
            if saw.power > power_threshold:
                result.append(saw)
        return result

    def find_all_with_brand(self, brand):
        # Повертає список пилок, які мають задану марку.
        result = []
        for saw in self.saw_list:
            if saw.brand == brand:
                result.append(saw)
        return result

    def find_all_with_remaining_work_time_greater_than(self, work_time_threshold):
        #Повертає список пилок, у яких залишковий час роботи більший за заданий поріг.
        result = []
        for saw in self.saw_list:
            if saw.get_remaining_work_time() > work_time_threshold:
                result.append(saw)
        return result

    def get_results_of_method(self, method_name):
        # Повертає список результатів виклику заданого методу для об'єктів пилок.
        return [getattr(saw, method_name)() for saw in self.saw_list if hasattr(saw, method_name)]

    def enumerate_saws(self):
        #Повертає список, що містить індекс та об'єкт кожної пилки.
        return [(index, saw) for index, saw in enumerate(self.saw_list)]

    def zip_results(self, method_name):
        #Повертає список, що містить об'єкт пилки та результат виклику заданого методу для цього об'єкта.
        return [(saw, getattr(saw, method_name)()) for saw in self.saw_list if hasattr(saw, method_name)]

    def get_attributes_by_type(self, attribute_type):
        #Повертає словник, що містить атрибути пилок, які є заданого типу.
        return {key: value for saw in self.saw_list for key, value in saw.__dict__.items() if isinstance(value, attribute_type)}

    def check_condition(self, condition):
        #Перевіряє, чи виконується задана умова для всіх або хоча б однієї пилки.
        return [saw for saw in self.saw_list if condition(saw)]





