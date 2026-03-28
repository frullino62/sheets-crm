import os
import json
from google.oauth2.service_account import Credentials
import gspread

SHEET_ID = os.environ["SHEET_ID"]

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# legge JSON da Render ENV
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=SCOPES
)

client = gspread.authorize(creds)


def sheet():
    return client.open_by_key(SHEET_ID).sheet1


def get_all():
    return sheet().get_all_records()


def add_cliente(nome, email):
    sheet().append_row([nome, email])


def delete_cliente(index):
    sheet().delete_rows(index + 2)  
    # +2 perché:
    # riga 1 = header
    # index parte da 0
