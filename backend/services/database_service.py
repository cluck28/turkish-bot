import os
from dotenv import load_dotenv
from time import sleep
from typing import Iterator
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy_utils import database_exists

Base = declarative_base()
load_dotenv()

USER = os.getenv("DB_USER")
PASS = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
NAME = os.getenv("DB_NAME")
PORT = os.getenv("DB_PORT")

Engine = None
SessionLocal = None

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{NAME}?sslmode=require"
)


def __connect_to_database() -> bool:
    try:
        if not database_exists(SQLALCHEMY_DATABASE_URL) and os.getenv("ENV") == "dev":
            engine = create_engine()
            conn = engine.connect()
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {NAME}"))
            conn.execute(text(f"CREATE USER IF NOT EXISTS {USER}"))
            conn.execute(text(f"GRANT ALL PRIVILEGES ON DATABASE {NAME} to {USER}"))
            conn.commit()
            conn.close()
            engine.dispose()
            return True
        elif database_exists(SQLALCHEMY_DATABASE_URL):
            return True
        else:
            return False
    except Exception:
        return False


def init_db():
    global Engine
    global SessionLocal
    conn = False
    period = 0
    while not conn and period < 10:
        conn = __connect_to_database()
        sleep(0.5)
        period += 1
    if not conn:
        raise Exception("Unable to establish database connection")
    Engine = create_engine(SQLALCHEMY_DATABASE_URL, max_overflow=-1)
    SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=Engine, expire_on_commit=False
    )
    return Engine


def tables_list() -> list[str]:
    return Base.metadata.tables.keys()


def get_db() -> Iterator[Session]:
    global SessionLocal
    if not SessionLocal:
        SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=Engine, expire_on_commit=False
        )
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_db_instance() -> Session:
    return next(get_db())


def clean_db():
    engine = init_db()
    with engine.connect() as conn:
        trans = conn.begin()
        for table in reversed(Base.metadata.sorted_tables):
            conn.execute(table.delete())
        trans.commit()


def create_db_tables():
    Base.metadata.create_all(bind=Engine)