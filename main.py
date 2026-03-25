from fastapi import FastAPI
from pydantic import BaseModel
import sheets_db

app = FastAPI()


class Cliente(BaseModel):

    nome: str
    email: str
    telefono: str


@app.get("/")
def home():

    return {"status": "CRM online"}


@app.get("/clienti")
def get_clienti():

    return sheets_db.get_all()


@app.post("/clienti")
def add_cliente(cliente: Cliente):

    sheets_db.add_row([
        cliente.nome,
        cliente.email,
        cliente.telefono
    ])

    return {"message": "cliente aggiunto"}


@app.delete("/clienti/{row_id}")
def delete_cliente(row_id: int):

    sheets_db.delete_row(row_id)

    return {"message": "cliente eliminato"}


@app.put("/clienti/{row_id}")
def update_cliente(row_id: int, cliente: Cliente):

    sheets_db.update_row(
        row_id,
        [
            cliente.nome,
            cliente.email,
            cliente.telefono
        ]
    )

    return {"message": "cliente aggiornato"}
