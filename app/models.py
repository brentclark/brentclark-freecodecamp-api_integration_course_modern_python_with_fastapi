from typing import Dict
from pydantic import StrictStr
from sqlmodel import Field
from sqlmodel import SQLModel
from sqlalchemy import JSON, Column


class TranslationTask(SQLModel, table=True):
    __tablename__ = "translation_tasks"
    id: int = Field(default=None, primary_key=True)
    text: StrictStr = Field(..., nullable=False)
    languages: dict = Field(default_factory=dict, sa_column=Column(JSON))
    status: StrictStr = Field(default="in progress")
