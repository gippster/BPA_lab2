
from bs4 import BeautifulSoup
import requests


def course() -> float:
    url = 'https://www.google.com/search?q=курс+доллара'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    # div class="BNeawe iBp4i AP7Wnd">81,79 Российский рубль"
    usd_course = ''
    usd = soup.findAll('div', class_='BNeawe iBp4i AP7Wnd')
    for data in usd:  # Находим курс доллара
        if data.find('div'):
            usd_course = data.text
    mean_of_course = float(usd_course.replace(",", ".").split()[0])
    if usd_course != '':
        return mean_of_course
