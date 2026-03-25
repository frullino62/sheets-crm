from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import sheets_db

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):

    clienti = sheets_db.get_all()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "clienti": clienti}
    )


@app.post("/add")
def add_cliente(
    nome: str = Form(...),
    email: str = Form(...),
    telefono: str = Form(...)
):

    sheets_db.add(nome, email, telefono)

    return {"status": "ok"}


@app.post("/delete")
def delete_cliente(row: int = Form(...)):

    sheets_db.delete(row)

    return {"status": "deleted"}
