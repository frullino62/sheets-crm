from google.oauth2.service_account import Credentials
import gspread

SHEET_ID = "10EU1gQSBbgA3k-n2ltzlJqW54NQ1aqBobHpvPdOfmsU"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
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
    sheet().delete_rows(index + 1)  # +1 perché header
