from fastapi import FastAPI
import sheets_db

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok"}


# 🔥 TEST GOOGLE SHEETS
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


@app.get("/clienti")
def get_clienti():
    return sheets_db.get_all()


@app.post("/clienti")
def add_cliente(nome: str, email: str):
    sheets_db.add_cliente(nome, email)
    return {"status": "cliente aggiunto"}


@app.delete("/clienti/{index}")
def delete_cliente(index: int):
    sheets_db.delete_cliente(index)
    return {"status": "cliente eliminato"}
