from pathlib import Path
from sqlmodel import create_engine
from sqlmodel import Session
from sqlmodel import SQLModel
from contextlib import contextmanager

DB_PATH = str((Path().parent / "database.db").resolve())
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> SQLModel:
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session():
    # Dependency function - yields Session object
    with Session(engine) as session:
        yield session
