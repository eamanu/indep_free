import pytest


@pytest.fixture()
def envs(mocker):
    mocker.patch.dict('os.environ', {'URL_NEWSPAPER': 'http://example.org',
                                     'TO_MAIL_LIST': 'mail1@mail.com,mail2@mail.com',
                                     'MAIL_SUBJECT': 'Mail Subject'})

