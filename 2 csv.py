import pandas as pd
import numpy as np

data = pd.read_csv('2 ex csv.csv',
                   sep=';',
                   parse_dates=['Первый визит', 'Последний визит'])

data[:4]

#parse_dates=['Первый визит', 'Последний визит']

composition = data['визиты'].str.split(';', expand=True).stack().str.strip().reset_index(level=1, drop=True)

composition = pd.DataFrame(composition,
                           columns=['visits_'])

crm = data.drop(['визиты'], axis=1).join(composition)

crm.to_excel('result_ex2.xlsx',
             sheet_name='crm',
             index=True)

