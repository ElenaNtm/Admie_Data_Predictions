# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 12:27:20 2023

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


"""
Net Load
"""
path_old = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_NET_LOAD_Production.csv"
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Daily_Net_Load.csv"
df_old = pd.read_csv(path_old, index_col = 'Date')
df = pd.read_csv(path, index_col = 'Date')

df.head()
df = pd.concat([df, df_old])
df.tail()
df.info()

with open(path, 'w', encoding = 'utf-8-sig') as f:
  df.to_csv(f)
"""
Lignite
"""
path_old = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_Lignite_Production.csv"
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).csv"

df_old = pd.read_csv(path_old, index_col = 'Date')
df = pd.read_csv(path, index_col = 'Date')


df = pd.concat([df, df_old])
df.tail()
df.info()

with open(path, 'w', encoding = 'utf-8-sig') as f:
  df.to_csv(f)

"""
Hydro
"""
path_old = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_Hydro_Production.csv"
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Hydro_Production.csv"

df_old = pd.read_csv(path_old, index_col = 'Date')
df = pd.read_csv(path, index_col = 'Date')


df = pd.concat([df, df_old])
df.tail()
df.info()

with open(path, 'w', encoding = 'utf-8-sig') as f:
  df.to_csv(f)
  
"""
RES
"""
path_old = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_RES_Production.csv"
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/RES_Production.csv"

df_old = pd.read_csv(path_old, index_col = 'Date')
df = pd.read_csv(path, index_col = 'Date')


df = pd.concat([df, df_old])
df.tail()
df.info()

with open(path, 'w', encoding = 'utf-8-sig') as f:
  df.to_csv(f)
  
"""
Gas
"""
path_old = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_Gas_Production.csv"
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Gas_Production.csv"

df_old = pd.read_csv(path_old, index_col = 'Date')
df = pd.read_csv(path, index_col = 'Date')


df = pd.concat([df, df_old])
df.tail()
df.info()

with open(path, 'w', encoding = 'utf-8-sig') as f:
  df.to_csv(f)
 
  
  

