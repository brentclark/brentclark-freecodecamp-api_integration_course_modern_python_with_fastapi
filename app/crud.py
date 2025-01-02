from typing import Annotated
from sqlmodel import Session, select
from fastapi import Depends

from app.models import TranslationTask

from app.db import get_session, engine
SessionDep = Annotated[Session, Depends(get_session)]


def create_translation_task(db: SessionDep, text: str, languages: list):
    task = TranslationTask(text=text, languages=languages)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task


def get_translation_task(db: SessionDep, task_id: int):
    statement = select(TranslationTask).where(TranslationTask.id == task_id)
    return db.exec(statement)


def update_translation_task(db: SessionDep, task_id: int, translations: dict):
    statement = select(TranslationTask).where(TranslationTask.id == task_id)
    if db.exec(statement):
        print("ok")
