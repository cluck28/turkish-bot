from datetime import datetime
from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from pydantic import ValidationError

from models.dictionary import WordDB, DictionaryDB
from schemas.dictionary import Word, WordResponse, DictionaryEntry, DictionaryEntryResponse
from schemas.shared_schemas import ErrorResponse
from services.util_service import create_unique_id


class Dictionary:
    def __init__(self, db: Session, correlation_id: Optional[str] = None):
        self.db: Session = db
        self.correlation_id: str | None = correlation_id