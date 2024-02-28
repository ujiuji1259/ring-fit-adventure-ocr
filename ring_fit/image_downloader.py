from datetime import date, datetime
from dataclasses import dataclass

from googleapiclient.discovery import build

from ring_fit.gcp_credential import get_credentials

@dataclass
class FitResultImage:
    drive_id: str
    name: str
    created_at: date
    raw_image: bytes

    def within_target_date(self, from_date: date, to_date: date) -> bool:
        return self.created_at >= from_date and self.created_at <= to_date

    @property
    def actioned_at(self):
        return datetime.strptime(self.name[:8], '%Y%m%d').date()


class FitResultImageDownloader:

    def __init__(self, drive_id: str):
        self.client = self._get_drive_client()
        self.drive_id = drive_id

    def _get_drive_client(self):
        creds = get_credentials('credentials.json')
        return build("drive", "v3", credentials=creds)

    def _download_image(self, drive_id: str) -> bytes:
        return self.client.files().get_media(fileId=drive_id).execute()

    def download_images(self, from_date: date, to_date: date):
        results = self.client.files().list(
            q=f"'{self.drive_id}' in parents",
            pageSize=10,
            fields="nextPageToken, files(id, name, createdTime)",
        ).execute().get('files', [])

        images = [
            FitResultImage(
                result['id'],
                result['name'],
                datetime.strptime(result['createdTime'], '%Y-%m-%dT%H:%M:%S.%fZ').date(),
                self._download_image(result['id']),
            )
            for result in results
        ]
        valid_images = [image for image in images if image.within_target_date(from_date, to_date)]
        return valid_images
