import pandas as pd
import numpy as np
import requests
import bs4


url = 'https://cbr.ru/currency_base/daily/?unidbquery.posted=True&unidbquery.to=03.08.2024#highlight=%D0%BA%D1%83%D1%80%D1%81%D1%8B%7C%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%7C%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B%7C%D0%BA%D1%83%D1%80%D1%81%D1%83%7C%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0'

source = requests.get(url).text
# soup = bs4.BeautifulSoup(source, 'html.parser')
soup = bs4.BeautifulSoup(source, 'lxml')
#table class
table = soup.select_one('.data')

hist_data = pd.read_html(str(table))

hist_data = hist_data[0]

hist_data.to_csv('result_ex3_currency.csv',
                 index=False)