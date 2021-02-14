import pytest


@pytest.mark.freeze_time('1991-08-12')
def test_get_current_date(envs):
    from indep_free.manager import get_current_date
    assert get_current_date() == '19910812'


