import os
import pytest

@pytest.fixture()
def envs(mocker):
    mocker.patch.dict(os.environ, {'URL_NEWSPAPER': 'http://example.org',
                                      'TO_MAIL_LIST': 'mail1@example.org,mail2@example.org',
                                      'MAIL_SUBJECT': 'MAIL SUBJECT'})
