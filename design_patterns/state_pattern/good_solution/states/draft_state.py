from states.state import State
from states.moderation_state import ModerationState

class DraftState(State):
    def __init__(self, document):
        self._document = document

    def publish(self):
        self._document.state = ModerationState(self._document)
