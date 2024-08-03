import pandas as pd
import numpy as np

#
data = pd.read_excel('ex_1_xls_imp.xlsx',
                     skiprows=5,
                     usecols='A:B')

#
data['Terr']=np.where(data['Name'].str.endswith('Гинеколог'),
                      data['Name'].str.split(' ', n=1).str[0],
                      np.nan)

data['Terr'] = data['Terr'].ffill()

data = data[data['Name'].notnull()]

data.to_excel('result_ex1.xlsx',
              sheet_name='sheet_nm',
              index=True)