from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import sheets_db

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    clienti = sheets_db.get_clienti()
    opere = sheets_db.get_opere()

    html = """
    <html>
    <head>
        <title>CRM PRO</title>
        <style>
            body { font-family: Arial; background:#0f172a; color:white; padding:20px; }
            .card { background:#1e293b; padding:20px; margin-bottom:20px; border-radius:10px; }
            input { padding:10px; margin:5px; border-radius:5px; border:none; }
            button { padding:10px; background:#22c55e; color:white; border:none; border-radius:5px; }
            .cliente { margin-bottom:15px; padding:10px; border-bottom:1px solid #334155; }
            .opera { margin-left:20px; font-size:14px; color:#cbd5f5; }
        </style>
    </head>
    <body>

    <h1>🚀 CRM RELAZIONALE</h1>

    <div class="card">
        <h2>Aggiungi Cliente</h2>
        <form action="/add_cliente">
            <input name="nome" placeholder="Nome" required>
            <input name="email" placeholder="Email" required>
            <button>Aggiungi</button>
        </form>
    </div>

    <div class="card">
        <h2>Aggiungi Opera</h2>
        <form action="/add_opera">
            <input name="cliente_id" placeholder="ID Cliente" required>
            <input name="barca" placeholder="Barca" required>
            <input name="opera" placeholder="Opera" required>
            <input name="tipo" placeholder="Tipo" required>
            <button>Aggiungi</button>
        </form>
    </div>

    <div class="card">
        <h2>Clienti + Opere</h2>
    """

    for c in clienti:
        cid = c.get("id")
        nome = c.get("nome")
        email = c.get("email")

        html += f"""
        <div class="cliente">
            <strong>{nome}</strong> ({email}) - ID: {cid}
        """

        opere_cliente = sheets_db.get_opere_by_cliente(cid)

        for o in opere_cliente:
            html += f"""
            <div class="opera">
                🚤 {o.get("barca")} → {o.get("opera")} ({o.get("tipo")})
            </div>
            """

        html += "</div>"

    html += """
    </div>
    </body>
    </html>
    """

    return html


@app.get("/add_cliente")
def add_cliente(nome: str, email: str):
    sheets_db.add_cliente(nome, email)
    return RedirectResponse("/", status_code=302)


@app.get("/add_opera")
def add_opera(cliente_id: str, barca: str, opera: str, tipo: str):
    sheets_db.add_opera(cliente_id, barca, opera, tipo)
    return RedirectResponse("/", status_code=302)
