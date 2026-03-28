from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import sheets_db

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    clienti = sheets_db.get_all()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "clienti": clienti
        }
    )


@app.get("/add")
def add(nome: str, email: str):
    sheets_db.add_cliente(nome, email)
    return {"status": "ok"}


@app.get("/delete/{index}")
def delete(index: int):
    sheets_db.delete_cliente(index)
    return {"status": "deleted"}


@app.get("/clienti")
def clienti():
    return {"status": "success", "records": sheets_db.get_all()}
