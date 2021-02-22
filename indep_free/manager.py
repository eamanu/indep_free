from datetime import date
from indep_free.downloader import get_newspaper
from typing import Union
from requests import Response
from pathlib import Path
from indep_free.mailer import send_mail


def get_current_date() -> str:
    "Get the current date in the format %Y%m%d"
    today = date.today()
    return date.strftime(today, '%Y%m%d')


def save_file(pdf: Response,
              filename: Path) -> bool:
    with open(filename, 'wb') as f:
        f.write(pdf.content)
    return True


def download_newspaper(download_folder: str,
                       remove_np_after_download: bool = True,
                       d_to_download: Union[bool, date] = False) -> bool:
    if d_to_download or remove_np_after_download:
        raise NotImplementedError
    else:
        date_to_download = get_current_date()

    pdf = get_newspaper(date_to_download)
    filename = Path(download_folder, date_to_download + '.pdf')

    save_file(pdf, filename)
    send_mail(filename, date_to_download)
    return True
