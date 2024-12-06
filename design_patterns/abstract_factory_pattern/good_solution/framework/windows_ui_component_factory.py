from abstract_factory_pattern.naive_solution.gui_framework.windows.windows_button import (
    WindowsButton,
)
from abstract_factory_pattern.naive_solution.gui_framework.windows.windows_checkbox import (
    WindowsCheckbox,
)
from abstract_factory_pattern.good_solution.framework.ui_component_factory import (
    UIComponentFactory,
)
from abstract_factory_pattern.naive_solution.gui_framework.button import Button
from abstract_factory_pattern.naive_solution.gui_framework.checkbox import Checkbox

class WindowsUIComponentFactory(UIComponentFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()
