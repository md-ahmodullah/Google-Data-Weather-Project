import requests
from bs4 import BeautifulSoup as bs

def get_scrape_weather_data(city):
    city = city.replace(' ', '+')
    url = f'https://www.google.com/search?q=weather+of+{city}'

    session = requests.Session()

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    LANGUAGE = 'en-GB,en-US;q=0.9,en;q=0.8'

    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE

    response = session.get(url)
    soup = bs(response.text, 'html.parser')

    results = {}

    results['location'] = soup.find('span', attrs={'class':'BBwThe'}).text
    results['weather'] = soup.find('span', attrs={'id': "wob_dc"}).text
    results['temperature'] = soup.find('span', attrs={'id': "wob_tm"}).text

    return results

# print(get_scrape_weather_data('new york'))