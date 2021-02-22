import pytest


def test_main(mocker, envs):
    from indep_free.cli import main
    mocker.patch('indep_free.cli.download_newspaper',
                 return_value=True)
    assert main()

