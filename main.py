import asyncio
from concurrent.futures import ThreadPoolExecutor

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from sheets import get_data

app = FastAPI()
templates = Jinja2Templates(directory="templates")
executor = ThreadPoolExecutor()


@app.get("/")
async def home(request: Request):
    """
    Route principale — usa async + executor per non bloccare il server
    durante la lettura del CSV da Google Sheets.
    """
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(executor, get_data)

    if not data:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "data": [], "error": "Dati non disponibili al momento. Riprova tra poco."}
        )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data}
    )


@app.get("/health")
async def health():
    """
    Endpoint di health check — utile per Render e per monitoraggio.
    Ritorna lo stato dell'app e il numero di record disponibili.
    """
    loop = asyncio.get_event_loop()
    try:
        data = await loop.run_in_executor(executor, get_data)
        return {"status": "ok", "records": len(data)}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
