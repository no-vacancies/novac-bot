import requests
from Corp._config import ENTRIES
from Corp.config import BASE_URL, LOSS_FORMAT
from Core.esi import get_id


def submit_srp(name, url, submitted_by, extra=None):
    params = {
        'usp': 'pp_url',
        ENTRIES['name']: name,
        ENTRIES['killmail_url']: url,
        ENTRIES['extra_info']: submitted_by}
    if extra:
        extra = extra.strip()
        params[ENTRIES['extra_info']] += ': ' + extra

    requests.post(BASE_URL, params=params)


def valid_lossmail(url):
    if LOSS_FORMAT in url and requests.get(url).status_code == 200:
        return True
    else:
        return False


def valid_character(name):
    try:
        get_id(name, 'character')
        return True
    except IndexError:
        return False
