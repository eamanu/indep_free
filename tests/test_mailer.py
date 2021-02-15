import pytest
import pathlib


def tests_get_message(envs):
    from indep_free.mailer import get_message
    date_to_download = '1991-08-12'
    message = 'Buenas\n\n Este mail corresponde al envío del diario con fecha '\
              f'{date_to_download}\n\nSaludos!'

    assert message == get_message(date_to_download)


def test_send_mail(mocker, envs):
    from indep_free.mailer import send_mail
    mocker.patch('indep_free.mailer.subprocess.call', return_value=True)
    p = pathlib.Path("/home/eamanu/test")
    assert send_mail(p, '1991-08-12')

