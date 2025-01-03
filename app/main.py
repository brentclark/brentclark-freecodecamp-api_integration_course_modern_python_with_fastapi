from typing import Annotated

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from icecream import ic
from sqlmodel import Session

from app.crud import create_translation_task, get_translation_task
from app.db import get_session, init_db
from app.schemas import TaskResponse, TranslationRequest, TranslationStatus
from app.utils import perform_translation

app = FastAPI(title="Moo")
templates = Jinja2Templates(directory="templates")
SessionDep = Annotated[Session, Depends(get_session)]

allowed_origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/translate", response_model=TaskResponse)
def translate(
    request: TranslationRequest, background_tasks: BackgroundTasks, db: SessionDep,
):
    task = create_translation_task(db, request.text, request.languages)
    background_tasks.add_task(
        perform_translation, task.id, request.text, request.languages,
    )
    return {"task_id": task.id}


@app.get("/translate/{task_id}", response_model=TranslationStatus)
def get_translate_status_by_id(task_id: int, db: SessionDep):
    task = get_translation_task(db, task_id)
    print(task)

    if not task:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="task not found")

    return {
        "task_id": task.id,
        "status": task.status,
        "translation": task.translation,
    }
