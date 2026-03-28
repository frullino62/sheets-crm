from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sheets_db

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    data = sheets_db.get_all()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data}
    )


@app.post("/update")
def update(row: int, nome: str, email: str, telefono: str):

    sheets_db.update(row, nome, email, telefono)

    return {"ok": True}


@app.post("/delete")
def delete(row: int):

    sheets_db.delete(row)

    return {"ok": True}
