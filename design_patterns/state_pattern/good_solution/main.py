from document import Document
from user_roles import UserRoles
from states.draft_state import DraftState

doc = Document(UserRoles.EDITOR)
print(doc.state.__class__.__name__)  # DraftState

doc.publish()
print(doc.state.__class__.__name__)  # ModerationState

doc.publish()
print(
    doc.state.__class__.__name__
)  # ModerationState -- editors can't create published documents

# Simulate Admin logging in and publishing the document
doc.current_user_role = UserRoles.ADMIN
doc.publish()
print(doc.state.__class__.__name__)  # PublishedState

# Can also switch to any state like so:
from states.draft_state import DraftState

doc.state = DraftState(doc)
print(doc.state.__class__.__name__)  # DraftState
