from typing import Dict
from consts import (
    CHANNELS,
    USERS,
    GET,
    POST,
    UNDEF,
    GENERIC_BLOCKS,
)
from utils.schemas import MessageParsedBody

class MessageRouter:
    """
    Determines which channel the message is in, parses the message
    to determine which function to call, and posts a response
    """

    def __init__(self, body: Dict):
        self.body = body
        self.channel_id = body["event"]["channel"]
        self.user_id = body["event"]["user"]
        self.text = body["event"]["text"]
        self.method = self._parse_method()
        self.blocks = self._get_blocks()
        self.message_ts = body["event"]["ts"]
        self.message_parsed_body = MessageParsedBody(
            channel_id=self.channel_id,
            channel_name=self.channel_name,
            message_ts=self.message_ts,
            user_id=self.user_id,
            user_name=self.user_name,
            text=self.text,
            method=self.method,
            blocks=self.blocks,
        )