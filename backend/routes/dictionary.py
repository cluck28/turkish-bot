from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from schemas.dictionary import DictionaryEntryResponse
from schemas.shared_schemas import ErrorResponse
from methods.dictionary import Dictionary
from services.database_service import get_db


router = APIRouter(prefix="/dictionary", tags=["Dictionary"])


@router.get("")
def get_all_words(request: Request, db: Session = Depends(get_db)):
    client = Dictionary(db=db)
    response: List[DictionaryEntryResponse] | ErrorResponse = client.get_all_words()
    if isinstance(response, ErrorResponse):
        return HTTPException(status_code=response.status_code, detail=response.detail)
    return JSONResponse(content=jsonable_encoder(response))