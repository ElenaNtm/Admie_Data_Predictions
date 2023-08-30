# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:20:21 2023

@author: Eleni
"""


"""
Load Libraries
"""

import pandas as pd
#import requests
from datetime import datetime, timedelta
#from datetime import datetime, timedelta
from urllib.error import HTTPError
import re

"""
Load the data
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).csv"
date_cols = ["Date"] 
df = pd.read_csv(path,index_col = 'Date', parse_dates = date_cols)
df.head()
df.info()
"""
Group by and sum by yearly production
"""
production = df.groupby(df.index.year)['Total Lignite in MWh'].sum()
print(production)
production.info()

df_production = production.reset_index()
df_production.columns = ['YEAR', 'ANUAL LIGNITE PRODUCTION IN MWh']
df_production.set_index('YEAR', inplace=True)
df_production.dropna()
"""
Save to csv
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Anual_Lignite_Production(MWh).csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_production.to_csv(f)