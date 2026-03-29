from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from auth import router as auth_router
import sheets_db

app = FastAPI()

app.include_router(auth_router)

from jinja2 import Environment, FileSystemLoader

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
templates.env = Environment(loader=FileSystemLoader("templates"), auto_reload=True)


@app.get("/")
def home(request: Request):
    try:
        clienti = sheets_db.get_all()
    except Exception as e:
        return {"errore": str(e)}  # debug

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "clienti": clienti
        }
    )

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@app.get("/add")
def add(nome: str, email: str):
    sheets_db.add_cliente(nome, email)
    return RedirectResponse(url="/", status_code=302)


@app.get("/delete/{index}")
def delete(index: int):
    sheets_db.delete_cliente(index)
    return RedirectResponse(url="/", status_code=302)


@app.get("/clienti")
def clienti():
    return {"status": "success", "records": sheets_db.get_all()}
