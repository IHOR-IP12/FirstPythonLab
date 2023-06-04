# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring
# pylint: disable=import-error
# pylint: disable=missing-class-docstring
# pylint: disable=attribute-defined-outside-init
from Models.RM import RM


class SM(RM):
    def __init__(self, rm_manager):
        super().__init__()
        self.rm_manager = rm_manager

    def __iter__(self):
        self.current_set = set()
        for saw in self.rm_manager:
            if hasattr(saw, 'data_set'):
                self.current_set.update(saw.data_set)
        self.iterator = iter(self.current_set)
        return self

    def __len__(self):
        return sum(len(saw.data_set) for saw in self.rm_manager if hasattr(saw, 'data_set'))

    def __getitem__(self, index):
        for saw in self.rm_manager:
            if hasattr(saw, 'data_set'):
                if index < len(saw.data_set):
                    return list(saw.data_set)[index]
                index -= len(saw.data_set)
        raise IndexError("Index out of range")

    def __next__(self):#використовується в ітераторах для отримання наступного елемента послідовност
        return next(self.iterator)
