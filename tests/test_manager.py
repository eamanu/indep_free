import pytest
from requests import Response


@pytest.mark.freeze_time('1991-08-12')
def test_get_current_date(envs):
    from indep_free.manager import get_current_date
    assert get_current_date() == '19910812'


def test_save_file(mocker, envs, tmpdir):
    from indep_free.manager import save_file

    class FakeResponse:
        def __init__(self):
            self.content = 'Test content'

    response = FakeResponse(
    )
    path_file = tmpdir / 'test.test'

    assert save_file(response, path_file)

    with path_file.open() as f:
        assert f.read() == 'Test content'



