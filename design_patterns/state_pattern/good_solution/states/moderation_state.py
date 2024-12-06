from states.state import State
from states.published_state import PublishedState
from user_roles import UserRoles

class ModerationState(State):
    def __init__(self, document):
        self._document = document

    def publish(self):
        if self._document.current_user_role == UserRoles.ADMIN:
            self._document.state = PublishedState(self._document)
