from fastapi import FastAPI
import sheets_db

app = FastAPI()


# 🔹 HOME (serve per capire se il server funziona)
@app.get("/")
def home():
    return {"status": "ok"}


# 🔹 TEST GOOGLE SHEETS
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


# 🔹 ENDPOINT CLIENTI (finale)
@app.get("/clienti")
def get_clienti():
    try:
        return sheets_db.get_all()
    except Exception as e:
        return {"error": str(e)}
