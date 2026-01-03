from sqlalchemy import Column, DateTime, String, func, ForeignKey
from sqlalchemy.orm import relationship

from services.database_service import Base


class WordDB(Base):
    __tablename__ = "words"

    word_id = Column(String, primary_key=True, index=True)
    word = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())

    dictionary_entry = relationship(
        "DictionaryDB", back_populates="words", cascade="all, delete-orphan", passive_deletes=True
    )

class DictionaryDB(Base):
    __tablename__ = "dictionary"

    dictionary_id = Column(String, primary_key=True, index=True)
    definition = Column(String, nullable=False)
    example = Column(String, nullable=False)
    grammar = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())

    word_id = Column(String, ForeignKey("words.word_id", ondelete="CASCADE"), unique=True)
    words = relationship("WordDB", back_populates="dictionary")
