import urllib.request
import json
from unittest.mock import patch
import pytest


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год
    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)
    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


date0 = {'currentDateTime': '01.03.2019T15:27Z'}


def test_get_cases0():
    with patch("json.load") as mocked_what_is_year_now:
        mocked_what_is_year_now.return_value = date0
        assert what_is_year_now() == 2019


date1 = {'currentDateTime': '2019-03-01T15:27Z'}


def test_get_cases1():
    with patch("json.load") as mocked_what_is_year_now:
        mocked_what_is_year_now.return_value = date1
        assert what_is_year_now() == 2019


date2 = {'currentDateTime': '2019/03/01T15:27Z'}


def test_get_cases2():
    with patch("json.load") as mocked_what_is_year_now:
        mocked_what_is_year_now.return_value = date2
        with pytest.raises(ValueError):
            what_is_year_now()
