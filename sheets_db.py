import gspread
from google.oauth2.service_account import Credentials
import os

SHEET_ID = os.environ["SHEET_ID"]

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

client = gspread.authorize(creds)

def sheet():
    return client.open_by_key(SHEET_ID).sheet1


def get_all():
    return sheet().get_all_records()


def add(nome, email, telefono):
    sheet().append_row([nome, email, telefono])


def update(row, nome, email, telefono):
    sheet().update(f"A{row}:C{row}", [[nome, email, telefono]])


def delete(row):
    sheet().delete_rows(row)
