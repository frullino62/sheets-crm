import os
import json
from google.oauth2.service_account import Credentials
import gspread

SHEET_ID = "10EU1gQSBbgA3k-n2ltzlJqW54NQ1aqBobHpvPdOfmsU"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=SCOPES
)

client = gspread.authorize(creds)
