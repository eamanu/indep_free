import requests
from indep_free.utils import URL_NEWSPAPER

class NotGetNewspaper(Exception):
    """"""
    def __init__(self, code, *args, **kwargs):
        self.message = f"I cannot get newspaper. Code error: {code}"
        super().__init__(self.message, *args, **kwargs)


def get_newspaper(name: str) -> requests.Response:
    """Download the newspaper with *name* into the *folder* directory.
    """
    pdf = requests.get(URL_NEWSPAPER.format(name), allow_redirects=True)
    if not pdf.ok:
        raise NotGetNewspaper(pdf.status_code)
    return pdf

