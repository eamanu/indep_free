import pytest


def test_get_newspaper_get_NotGetNewspaper(mocker, envs):
    from indep_free.downloader import get_newspaper
    from indep_free.downloader import NotGetNewspaper

    class FakeResponse:
        def __init__(self):
            self.ok = False
            self.status_code = 404

    mocker.patch('indep_free.downloader.requests.get', return_value=FakeResponse())

    with pytest.raises(NotGetNewspaper):
        get_newspaper('test')

