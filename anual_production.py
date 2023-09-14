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
from datetime import datetime, timedelta
#from urllib.error import HTTPError
#import re

"""
Load the data
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Daily_Net_Load.csv"
date_cols = ["Date"] 
df = pd.read_csv(path,index_col = 'Date', parse_dates = date_cols)
df.tail()
df.info()
"""
Group by and sum by yearly production
"""
production = df.groupby(df.index.year)['Total Net Load'].sum()
print(production)
production.info()

df_production = production.reset_index()
df_production.columns = ['YEAR', 'ANUAL NET LOAD']
df_production.set_index('YEAR', inplace=True)
df_production.head()
"""
Save to csv
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Anual_Net_Load.csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_production.to_csv(f)
  
"""
Lignite
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).csv"
date_cols = ["Date"] 
df = pd.read_csv(path,index_col = 'Date', parse_dates = date_cols)
production = df.groupby(df.index.year)['Total Lignite in MWh'].sum()
print(production)
production.info()

df_production = production.reset_index()
df_production.columns = ['YEAR', 'ANUAL LIGNITE PRODUCTION']
df_production.set_index('YEAR', inplace=True)
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Anual_Lignite_Production(MWh).csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_production.to_csv(f)
  
"""
Hydro
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Hydro_Production.csv"
date_cols = ["Date"] 
df = pd.read_csv(path,index_col = 'Date', parse_dates = date_cols)
#df.tail()
#df.info()
production = df.groupby(df.index.year)['Total Hydro'].sum()
print(production)
production.info()

df_production = production.reset_index()
df_production.columns = ['YEAR', 'ANUAL NET LOAD']
df_production.set_index('YEAR', inplace=True)
#df_production.dropna()  
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Anual_Hydro_Production.csv"

with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_production.to_csv(f)  
  
"""
Gas
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Gas_Production.csv"
date_cols = ["Date"] 
df = pd.read_csv(path,index_col = 'Date', parse_dates = date_cols)
#df.tail()
#df.info()
production = df.groupby(df.index.year)['Total Gas'].sum()
print(production)
production.info()

df_production = production.reset_index()
df_production.columns = ['YEAR', 'ANUAL GAS']
df_production.set_index('YEAR', inplace=True)
#df_production.dropna()  
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Anual_Gas_Production.csv"

with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_production.to_csv(f)    
  
"""
RES
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/RES_Production.csv"
date_cols = ["Date"] 
df = pd.read_csv(path,index_col = 'Date', parse_dates = date_cols)
#df.tail()
#df.info()
production = df.groupby(df.index.year)['Total RES'].sum()
print(production)
production.info()

df_production = production.reset_index()
df_production.columns = ['YEAR', 'ANUAL RES']
df_production.set_index('YEAR', inplace=True)
#df_production.dropna()  
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Anual_RES_Production.csv"

with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_production.to_csv(f)    