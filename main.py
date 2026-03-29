from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import sheets_db

app = FastAPI()

print("BASE_DIR:", BASE_DIR)
print("FILES:", os.listdir(BASE_DIR))
print("TEMPLATES:", os.listdir(os.path.join(BASE_DIR, "templates")))

import os

BASE_DIR = os.path.dirname(__file__)
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "clienti": []
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
