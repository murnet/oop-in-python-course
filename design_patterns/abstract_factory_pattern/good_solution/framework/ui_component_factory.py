from abstract_factory_pattern.naive_solution.gui_framework.button import Button
from abstract_factory_pattern.naive_solution.gui_framework.checkbox import Checkbox
from abc import ABC, abstractmethod

class UIComponentFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
