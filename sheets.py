import os
import time
import pandas as pd

# URL from environment variable (fallback to hardcoded for local dev)
URL = os.environ.get(
    "SHEET_URL",
    "https://docs.google.com/spreadsheets/d/10EU1gQSBbgA3k-n2ltzlJqW54NQ1aqBobHpvPdOfmsU/export?format=csv"
)

# Simple in-memory cache
_cache = {"data": None, "ts": 0}
CACHE_TTL = 60  # secondi prima di rileggere il foglio

def get_data():
    """
    Legge i dati dal foglio Google con cache e gestione degli errori.
    - Ritorna dati freschi ogni CACHE_TTL secondi
    - In caso di errore, ritorna i dati in cache (se disponibili) o lista vuota
    """
    now = time.time()
    cache_expired = now - _cache["ts"] > CACHE_TTL

    if _cache["data"] is None or cache_expired:
        try:
            df = pd.read_csv(URL)
            _cache["data"] = df.to_dict(orient="records")
            _cache["ts"] = now
            print(f"[sheets] Dati aggiornati: {len(_cache['data'])} righe")
        except Exception as e:
            print(f"[sheets] Errore nel leggere il foglio: {e}")
            # Ritorna i dati in cache anche se scaduti, oppure lista vuota
            return _cache["data"] or []

    return _cache["data"]
