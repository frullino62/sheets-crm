import os
import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    {
        "type": "service_account",
        "project_id": os.environ["GOOGLE_PROJECT_ID"],
        "private_key": os.environ["GOOGLE_PRIVATE_KEY"].replace("\\n", "\n"),
        "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
        "token_uri": "https://oauth2.googleapis.com/token",
    },
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
