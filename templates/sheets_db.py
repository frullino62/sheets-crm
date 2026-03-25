import gspread
from google.oauth2.service_account import Credentials

SHEET_NAME = "CRM"

def get_sheet():

    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=scope
    )

    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).sheet1

    return sheet


def get_all():

    sheet = get_sheet()
    data = sheet.get_all_records()

    return data


def add_row(values):

    sheet = get_sheet()
    sheet.append_row(values)


def delete_row(index):

    sheet = get_sheet()
    sheet.delete_rows(index)


def update_row(index, values):

    sheet = get_sheet()
    sheet.update(f"A{index}", [values])
