from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine

DB_PATH = str((Path().parent / "database.db").resolve())
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    with Session(engine) as session:
        yield session
