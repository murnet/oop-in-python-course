from document_states import DocumentStates
from user_roles import UserRoles

class Document:
    def __init__(self, state: DocumentStates, current_user_role: UserRoles):
        self.state = state
        self.current_user_role = current_user_role

    def publish(self):
        if self.state == DocumentStates.DRAFT:
            self.state = DocumentStates.MODERATION
        elif self.state == DocumentStates.MODERATION:
            if self.current_user_role == UserRoles.ADMIN:
                self.state = DocumentStates.PUBLISHED
        elif self.state == DocumentStates.PUBLISHED:
            # Do nothing
            pass
