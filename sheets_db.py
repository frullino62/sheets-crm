import os
import json
import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = "10EU1gQSBbgA3k-n2ltzlJqW54NQ1aqBobHpvPdOfmsU"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_client():
    creds_json = os.getenv("GOOGLE_CREDENTIALS")
    creds_dict = json.loads(creds_json)

    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=SCOPES   # 🔥 QUESTA È LA FIX
    )

    return gspread.authorize(creds)

def sheet():
    client = get_client()
    return client.open_by_key(SHEET_ID).sheet1

def get_all():
    return sheet().get_all_records()
