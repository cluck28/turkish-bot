import uvicorn
from fastapi import FastAPI

from services.database_service import init_db
from routes import (
    dictionary,
)

app = FastAPI()


init_db()


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


app.include_router(dictionary.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)