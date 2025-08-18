"""Very small rule-based chatbot used for tests.

The goal of this module is not to be state of the art but to showcase how a
backend can encapsulate the logic for generating replies.  A couple of canned
answers are provided for common greetings.  Additional responses can be taught
at runtime and stored in the database to simulate lightweight learning.  This
keeps the behaviour deterministic and lightweight so the test-suite can run
quickly.
"""

from sqlalchemy.orm import Session

from . import crud


RESPONSES = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist?",
    "bye": "Goodbye!",
}


def generate_response(message: str, db: Session | None = None) -> str:
    """Return a deterministic response for ``message``.

    If ``db`` is provided, user-taught responses are checked first.
    """

    if db is not None:
        learned = crud.find_knowledge(db, message)
        if learned is not None:
            return learned.response

    lowered = message.lower()
    for trigger, reply in RESPONSES.items():
        if trigger in lowered:
            return reply
    return f"You said: {message}"

