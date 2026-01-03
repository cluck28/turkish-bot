from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class Word(BaseModel):
    word: str

    model_config = ConfigDict(from_attributes=True)


class WordResponse(Word):
    word_id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DictionaryEntry(Word):
    word_id: str
    definition: str
    example: Optional[str]
    grammar: str

    model_config = ConfigDict(from_attributes=True)


class DictionaryEntryResponse(DictionaryEntry):
    dictionary_id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
