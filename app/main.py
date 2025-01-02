from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from sqlmodel import Session

from app.db import get_session, init_db

from app.schemas import TranslationRequest, TranslationStatus, TaskResponse
from app.crud import create_translation_task
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
def translate(request: TranslationRequest, db: SessionDep):
    task = create_translation_task(db, request.text, request.languages)
    BackgroundTasks.add_task(perform_translation, task.id, request.text, request.languages,  db)
    ic(request)
    return {"task_id": 1}
