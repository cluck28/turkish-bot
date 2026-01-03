from typing import Optional
from sqlalchemy.orm import Session



class Dictionary:
    def __init__(self, db: Session, correlation_id: Optional[str] = None):
        self.db: Session = db
        self.correlation_id: str | None = correlation_id