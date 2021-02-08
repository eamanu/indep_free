import subprocess

from pathlib import Path
from indep_free.utils import (
    MAIL_SUBJECT,
    TO_MAIL_LIST,
)


def get_message(date_to_download: str) -> str:
    return 'Buenas\n\n Este mail corresponde al envío del diario con fecha '\
           f'{date_to_download}\n\nSaludos!'


def send_mail(path: Path, date_to_download: str) -> bool:
    for email in TO_MAIL_LIST:
        cmd = ["mutt", "-a", path, "-s", MAIL_SUBJECT, email, "<",
               get_message(date_to_download)]

        subprocess.call(cmd)

