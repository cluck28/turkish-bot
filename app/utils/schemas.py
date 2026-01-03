from pydantic import BaseModel
from typing import List, Dict


class ParsedBody(BaseModel):
    channel_id: str
    channel_name: str
    user_id: str
    user_name: str
    message_ts: str


class MessageParsedBody(ParsedBody):
    text: str
    method: str
    blocks: List[Dict]