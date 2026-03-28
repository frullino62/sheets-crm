from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import sheets_db

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    try:
        clienti = sheets_db.get_all()
    except Exception as e:
        return {"errore": str(e)}

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "clienti": clienti
        }
    )


@app.get("/test")
def test():
    try:
        data = sheets_db.get_all()
        return {
            "status": "success",
            "records": data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


@app.get("/add")
def add_cliente(nome: str, email: str):
    sheets_db.add_cliente(nome, email)
    return RedirectResponse(url="/", status_code=303)


@app.get("/delete/{index}")
def delete_cliente(index: int):
    sheets_db.delete_cliente(index)
    return RedirectResponse(url="/", status_code=303)
