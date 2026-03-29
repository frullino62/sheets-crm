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
        <style>
            body {
                font-family: Arial;
                background: #f5f7fa;
                padding: 40px;
            }
            h1 {
                color: #333;
            }
            .container {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            }
            form {
                margin-bottom: 20px;
            }
            input {
                padding: 10px;
                margin-right: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                padding: 10px 15px;
                border: none;
                background: #4CAF50;
                color: white;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background: #45a049;
            }
            .cliente {
                display: flex;
                justify-content: space-between;
                padding: 10px;
                border-bottom: 1px solid #eee;
            }
            .delete {
                color: red;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>CRM Clienti</h1>

            <form action="/add">
                <input type="text" name="nome" placeholder="Nome" required>
                <input type="email" name="email" placeholder="Email" required>
                <button type="submit">Aggiungi</button>
            </form>

    """

    for i, c in enumerate(clienti):
        nome = c.get("nome", "")
        email = c.get("email", "")
        html += f"""
            <div class="cliente">
                <span>{nome} - {email}</span>
                <a class="delete" href="/delete/{i}">❌</a>
            </div>
        """

    html += """
        </div>
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
