from functions.level_1.two_date_parser import compose_datetime_from
from datetime import datetime


def test_compose_datetime_from():
    date = compose_datetime_from('Bla-bla', '11:15')
    today = datetime.today()
    assert date == datetime(today.year, today.month, today.day, int(date.hour), int(date.minute))
    date = compose_datetime_from('tomorrow', '13:40')
    assert date == datetime(today.year, today.month, today.day + 1, int(date.hour), int(date.minute))
    