# from gui_framework.operating_system_type import OperatingSystemType
from ..app.user_settings_form import UserSettingsForm
from ..gui_framework.operating_system_type import OperatingSystemType

os = OperatingSystemType.MAC  # Set the operating system type

user_settings_form = UserSettingsForm()
user_settings_form.render(os)

# Logs:
# Mac: render button
# Mac: render checkbox
