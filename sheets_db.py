import os
import json
import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = "10EU1gQSBbgA3k-n2ltzlJqW54NQ1aqBobHpvPdOfmsU"

def get_sheet():
    creds_json = os.getenv("GOOGLE_CREDENTIALS")

    if not creds_json:
        raise Exception("GOOGLE_CREDENTIALS non trovato")

    creds_dict = json.loads(creds_json)

    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
    )

    client = gspread.authorize(creds)
    return client.open_by_key(SHEET_ID).sheet1


def get_all():
    sheet = get_sheet()
    return sheet.get_all_records()
