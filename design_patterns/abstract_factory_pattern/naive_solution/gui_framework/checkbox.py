from abstract_factory_pattern.naive_solution.gui_framework.ui_component import (
    UIComponent,
)
from abc import abstractmethod

class Checkbox(UIComponent):
    """Interface for a checkbox UI component"""

    @abstractmethod
    def on_select(self):
        """Handle the checkbox select event"""
        pass

    # Other methods specific to checkboxes can be defined here...
