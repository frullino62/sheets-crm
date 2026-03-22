import pandas as pd

URL = "https://docs.google.com/spreadsheets/d/10EU1gQSBbgA3k-n2ltzlJqW54NQ1aqBobHpvPdOfmsU/export?format=csv"

def get_data():
    df = pd.read_csv(URL)
    return df.to_dict(orient="records")
