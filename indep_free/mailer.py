import subprocess

from pathlib import Path
from indep_free.utils import (
    MAIL_SUBJECT,
    TO_MAIL_LIST,
)
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



def upload_file(path: Path) -> str:
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    file1 = drive.CreateFile({'title': path.name})
    file1.SetContentFile(str(path))
    file1.Upload()
    file1.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'})
    return file1['alternateLink']


def get_message(date_to_download: str, path: Path) -> str:
    link = upload_file(path)
    return 'Buenas\n\n Este mail corresponde al envío del diario con fecha '\
           f'{date_to_download}\n\nDescargar desde el siguiente link: {link}\n\nSaludos!'


def send_mail(path: Path, date_to_download: str) -> bool:
    for email in TO_MAIL_LIST:
        cmd = ["echo", get_message(date_to_download, path), "mutt",
               "-s", MAIL_SUBJECT, '--', email]

        subprocess.call(cmd)
    return True

