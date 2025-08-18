"""Very small rule-based chatbot used for tests.

The goal of this module is not to be state of the art but to showcase how a
backend can encapsulate the logic for generating replies.  A couple of canned
answers are provided for common greetings and a sensible fallback is used for
unknown inputs.  This keeps the behaviour deterministic and lightweight so the
test-suite can run quickly.
"""

RESPONSES = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist?",
    "bye": "Goodbye!"
}


def generate_response(message: str) -> str:
    """Return a simple deterministic response for ``message``."""
    lowered = message.lower()
    for trigger, reply in RESPONSES.items():
        if trigger in lowered:
            return reply
    return f"You said: {message}"
