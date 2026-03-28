from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse

router = APIRouter()

# database temporaneo utenti (in memoria)
users = {}


@router.post("/register")
def register(email: str = Form(...), password: str = Form(...)):
    users[email] = password
    return RedirectResponse(url="/login", status_code=302)


@router.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    if users.get(email) == password:
        response = RedirectResponse(url="/", status_code=302)
        response.set_cookie(key="user", value=email)
        return response
    return {"error": "invalid login"}
