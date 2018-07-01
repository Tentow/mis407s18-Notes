import requests
from urllib.parse import quote_plus


def get_temp(city='Ames'):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID=06e81d1e5ef8943f21e81cc0d314d658'.format(quote_plus(city)))
    wdata = r.json()
    return float(wdata['main']['temp']) * 9/5 - 459.67
