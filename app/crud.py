from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, select

from app.db import engine, get_session
from app.models import TranslationTask

SessionDep = Annotated[Session, Depends(get_session)]


def create_translation_task(db: SessionDep, text: str, languages: list):
    task = TranslationTask(text=text, languages=languages)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task


def get_translation_task(db: SessionDep, task_id: int):
    get_translate_status_by_id = select(TranslationTask).where(
        TranslationTask.id == task_id,
    )
    return db.exec(get_translate_status_by_id).one_or_none()


# def update_translation_task(db: SessionDep, task_id: int, translations: dict):
def update_translation_task(task_id: int, translations: dict):
    with Session(engine) as db:
        task = select(TranslationTask).where(TranslationTask.id == task_id)
        results = db.exec(task)
        text = results.one()
        # ic("Text:", text)
        text.translation = translations
        text.status = "completed"
        db.add(text)
        db.commit()
        db.refresh(text)
        # ic("Updated text:", text)
