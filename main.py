from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import sheets_db

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    try:
        clienti = sheets_db.get_all()
    except Exception as e:
        return f"<h1>Errore: {str(e)}</h1>"

    html = """
    <html>
    <head>
        <title>CRM</title>
    </head>
    <body>
        <h1>Clienti</h1>

        <form action="/add">
            Nome: <input type="text" name="nome">
            Email: <input type="text" name="email">
            <button type="submit">Aggiungi</button>
        </form>

        <ul>
    """

    for i, c in enumerate(clienti):
        nome = c.get("nome", "")
        email = c.get("email", "")
        html += f"<li>{nome} - {email} <a href='/delete/{i}'>❌</a></li>"

    html += """
        </ul>
    </body>
    </html>
    """

    return html


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
    return {
        "status": "success",
        "records": sheets_db.get_all()
    }
