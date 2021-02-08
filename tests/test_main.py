import pytest

from indep_free.cli import main

def test_main(mocker):
    mocker.patch('indep_free.cli.main.download_newspaper',
                 return_value=True)
    assert main()
