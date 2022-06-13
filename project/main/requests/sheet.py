import os
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def get_service_sacc():
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds_json = os.path.join(os.path.dirname(__file__), 'service_account.json')

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def get_sheet(sheet_id = None):
    if sheet_id is None: sheet_id = os.environ.get('GOOGLE_SHEET_ID')
    resp = get_service_sacc().spreadsheets().values().get(spreadsheetId=sheet_id, range="A:D").execute()
    keys = ['id','order_id', 'price_dollor', 'delivery_date']
    data = [{key: value for key, value in zip(keys, row)} for row in resp['values'][1:]]
    return data
