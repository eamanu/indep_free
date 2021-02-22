import pytest

from requests import Response
from datetime import date


@pytest.mark.freeze_time('1991-08-12')
def test_get_current_date(envs):
    from indep_free.manager import get_current_date
    assert get_current_date() == '19910812'


def test_save_file(mocker, envs, tmpdir):
    from indep_free.manager import save_file

    class FakeResponse:
        def __init__(self):
            self.content = b'Test content'

    response = FakeResponse(
    )
    path_file = tmpdir / 'test.test'

    assert save_file(response, path_file)

    with path_file.open() as f:
        assert f.read() == 'Test content'

def test_raises_errors(envs):
    from indep_free.manager import download_newspaper

    with pytest.raises(NotImplementedError):
        assert download_newspaper('test', True, False)
        assert download_newspaper('test', False, date(1991, 8, 12))
        assert download_newspaper('test', True, date(1991, 8, 12))


@pytest.mark.freeze_time('1991-08-12')
def test_download_newspaper(mocker, envs):
    from indep_free.manager import download_newspaper
    mocker.patch('indep_free.manager.send_mail', return_value=True)
    mocker.patch('indep_free.manager.save_file', return_value=True)
    assert download_newspaper('test', False, False)
