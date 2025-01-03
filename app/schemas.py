from pydantic import BaseModel, PositiveInt, StrictStr


class TranslationRequest(BaseModel):
    text: StrictStr
    languages: list[StrictStr]


class TaskResponse(BaseModel):
    task_id: PositiveInt


class TranslationStatus(BaseModel):
    task_id: PositiveInt
    status: StrictStr
    translation: dict[StrictStr, StrictStr]
