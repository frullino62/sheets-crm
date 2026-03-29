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
        <title>CRM PRO</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #0f172a;
                color: #fff;
                margin: 0;
                padding: 0;
            }

            .container {
                max-width: 900px;
                margin: auto;
                padding: 30px;
            }

            h1 {
                text-align: center;
                margin-bottom: 30px;
            }

            .card {
                background: #1e293b;
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 20px;
            }

            input {
                padding: 12px;
                border-radius: 8px;
                border: none;
                margin-right: 10px;
                width: 200px;
            }

            button {
                padding: 12px 18px;
                border-radius: 8px;
                border: none;
                background: #22c55e;
                color: white;
                cursor: pointer;
            }

            button:hover {
                background: #16a34a;
            }

            .search {
                width: 100%;
                margin-bottom: 20px;
                padding: 12px;
                border-radius: 8px;
                border: none;
            }

            .cliente {
                display: flex;
                justify-content: space-between;
                padding: 15px;
                border-bottom: 1px solid #334155;
            }

            .delete {
                color: #ef4444;
                text-decoration: none;
                font-weight: bold;
            }

            .delete:hover {
                color: #dc2626;
            }
        </style>

        <script>
            function searchClient() {
                let input = document.getElementById("search").value.toLowerCase();
                let items = document.getElementsByClassName("cliente");

                for (let i = 0; i < items.length; i++) {
                    let text = items[i].innerText.toLowerCase();
                    items[i].style.display = text.includes(input) ? "" : "none";
                }
            }
        </script>
    </head>

    <body>
        <div class="container">

            <h1>🚀 CRM PRO</h1>

            <div class="card">
                <form action="/add">
                    <input type="text" name="nome" placeholder="Nome" required>
                    <input type="email" name="email" placeholder="Email" required>
                    <button type="submit">Aggiungi</button>
                </form>
            </div>

            <input id="search" class="search" placeholder="🔎 Cerca cliente..." onkeyup="searchClient()">

            <div class="card">
    """

    for i, c in enumerate(clienti):
        nome = c.get("nome", "")
        email = c.get("email", "")

        html += f"""
        <div class="cliente">
            <span>{nome} - {email}</span>
            <a class="delete" href="/delete/{i}">✖</a>
        </div>
        """

    html += """
            </div>

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
