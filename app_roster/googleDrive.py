import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from typing import Final
from typing import List

SCOPES: Final[List] = [
    'https://www.googleapis.com/auth/drive.metadata.readonly'
]
SHARED_DRIVE_ID: Final[str] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
DIRECTORY_ID: Final[str] = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
FILENAME: Final[str] = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

def get_credentials(scopes: List):
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            credentials = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    return credentials

def directory_files(filename: str, directory_id: str,
                    pages_max: int = 10) -> List:
    """
    対象のディレクトリ配下からファイル名で検索した結果を配列で返す
    :param filename: ファイル名
    :param directory_id: ディレクトリID
    :param pages_max: 最大ページ探索数
    :return: ファイルリスト
    """
    credentials = get_credentials(SCOPES)
    service = build("drive", "v3", credentials=credentials)
    items: List = []
    page = 0
    while True:
        page += 1
        if page == pages_max:
            break
        results = service.files().list(
            corpora="drive",
            driveId=SHARED_DRIVE_ID,
            includeItemsFromAllDrives=True,
            includeTeamDriveItems=True,
            q=f"'{directory_id}' in parents and "
              f"name = '{filename}' and "
              "trashed = false",
            supportsAllDrives=True,
            pageSize=10,
            fields="nextPageToken, files(id, name)").execute()
        items += results.get("files", [])

        page_token = results.get('nextPageToken', None)
        if page_token is None:
            break
    return items

items = drive_util.directory_files(
    filename=FILENAME,
    directory_id=DIRECTORY_ID)
for item in items:
    print(f"{item['id']} : {item['name']}")