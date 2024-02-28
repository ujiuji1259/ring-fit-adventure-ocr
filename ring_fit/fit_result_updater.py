from datetime import date

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from ring_fit.fit_result import FitResult
from ring_fit.gcp_credential import get_credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def preprocess_fit_result(actions: list[FitResult], actioned_at: date) -> list[list[str]]:
    return [
        [
            action.fit_skill.name,
            action.fit_skill.type.value,
            action.reps,
            actioned_at.strftime("%Y/%m/%d"),
        ] 
        for action in actions
    ]


class FitSkillUpdater:

    def __init__(self, sheet_id: str, sheet_name: str):
        self.sheet = self._get_sheet_client()
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name

    def _get_sheet_client(self):
        creds = get_credentials('credentials.json')
        service = build("sheets", "v4", credentials=creds)
        return service.spreadsheets()

    def append(self, actions: list[FitResult], actioned_at: date):
        sheet_range = f'{self.sheet_name}!A2:D'
        body = {
            'range': sheet_range,
            'majorDimension': 'ROWS',
            'values': preprocess_fit_result(actions, actioned_at),
        }
        _ = (
            self.sheet.values()
            .append(
                spreadsheetId=self.sheet_id,
                range=sheet_range,
                body=body,
                valueInputOption='RAW',
                insertDataOption='INSERT_ROWS')
            .execute()
        )
