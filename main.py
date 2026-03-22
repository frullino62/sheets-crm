from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sheets import get_data

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):

    data = get_data()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data}
    )
