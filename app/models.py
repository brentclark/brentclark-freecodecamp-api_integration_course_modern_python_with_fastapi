from pydantic import StrictStr
from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


class TranslationTask(SQLModel, table=True):
    __tablename__ = "translation_tasks"
    id: int = Field(default=None, primary_key=True)
    text: StrictStr = Field(..., nullable=False)
    languages: dict = Field(default_factory=dict, sa_column=Column(JSON))
    status: StrictStr = Field(default="in progress")
    translations: dict = Field(default_factory=dict, sa_column=Column(JSON))
