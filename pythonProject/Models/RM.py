# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring
# pylint: disable=import-error
# pylint: disable=missing-class-docstring
# pylint: disable=useless-super-delegation
# pylint: disable=too-few-public-methods
from abc import ABC
from Managers.saw_manager import SawManager


class RM(SawManager, ABC):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        return iter(self.saw_list)
