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


def clienti_sheet():
    return client.open_by_key(SHEET_ID).worksheet("Clienti")


def opere_sheet():
    return client.open_by_key(SHEET_ID).worksheet("Opere")


# -------- CLIENTI --------

def get_clienti():
    return clienti_sheet().get_all_records()


def add_cliente(nome, email):
    clienti = get_clienti()
    new_id = len(clienti) + 1
    clienti_sheet().append_row([new_id, nome, email])


def delete_cliente(index):
    clienti_sheet().delete_rows(index + 2)


# -------- OPERE --------

def get_opere():
    return opere_sheet().get_all_records()


def add_opera(cliente_id, barca, opera, tipo):
    opere = get_opere()
    new_id = len(opere) + 1
    opere_sheet().append_row([new_id, cliente_id, barca, opera, tipo])


# -------- RELAZIONI --------

def get_opere_by_cliente(cliente_id):
    opere = get_opere()
    return [o for o in opere if str(o.get("cliente_id")) == str(cliente_id)]
