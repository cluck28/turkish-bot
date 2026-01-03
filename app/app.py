import logging
from slack_bolt import App, Say, Ack, Respond
from typing import Dict
from router import MessageRouter, ActionRouter, FileRouter


app = App()


@app.event({"type": "message", "subtype": None})
def reply_in_thread(body: Dict, say: Say):
    """
    Generic listener for messages
    """
    router = MessageRouter(body)
    payload = router.run()
    blocks = payload.get("blocks", None)
    say(blocks=blocks, text="")