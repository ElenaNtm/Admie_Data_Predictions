# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:21:51 2023

@author: Eleni
"""

#generate all the urls
def generate_urls1(start_date, end_date):
    base_url = "https://www.admie.gr/sites/default/files/attached-files/type-file/"
    date_format = "%Y/%m/%Y%m%d"  # This is the desired format
    delta = timedelta(days=1)
    current_date = start_date

    while current_date <= end_date:
        url_date = current_date.strftime(date_format)
        url = f"{base_url}{url_date}_SystemRealizationSCADA_01.xls"
        yield url
        current_date += delta        
        
        

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
Open the file that we have already created and the list with the dropped indexes
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).csv"
df_lignite = pd.read_csv(path, index_col = 'Date')
df_lignite.head()

txt_path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/lignite_indices_where_zero.txt"
with open(txt_path, 'r') as file:
    lines = file.readlines()  # Read all lines from the file
print(lines)
dropped = [line.replace("'", "").replace("-", "").replace("\n", "") for line in lines]

#print(dropped)

 
"""
Loop the urls
"""
#Initialize an empty list for the non existing urls
non_existan_urls = []

# Initialize an empty DataFrame
df = pd.DataFrame()

"""
Οι υπόλοιπες ημ/νιες από 01/08/2020 δεν έχουν κάποιο θέμα εκτός από τη τελευταία μέρα του μήνα το οποίο θα το λύσουμε
θα το σπάσουμε ανά χρόνο γιατί κρασάρει η διαδικασία αλλιώς
"""
base_url = "https://www.admie.gr/sites/default/files/attached-files/type-file/"
"""
1ο έτος
"""

#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2020, 8, 1)
end_date = datetime(2020, 9, 1)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[45:46,26]
        df1 = df1.rename(index={45: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)

    # Increment to the next date
    current_date += timedelta(days=1)
#df.tail()
###############################################################################
#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2020, 9, 2)
end_date = datetime(2020, 9, 30)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[45:46,26]
        df1 = df1.rename(index={45: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)

    # Increment to the next date
    current_date += timedelta(days=1)
###############################################################################
start_date = datetime(2020, 10, 1)
end_date = datetime(2020, 10, 20)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[45:46,26]
        df1 = df1.rename(index={45: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)
        
    # Increment to the next date
    current_date += timedelta(days=1)       
###############################################################################
start_date = datetime(2020, 10, 21)
end_date = datetime(2020, 10, 31)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[45:46,26]
        df1 = df1.rename(index={45: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)
        
    # Increment to the next date
    current_date += timedelta(days=1)      
        
###############################################################################

start_date = datetime(2020, 11, 1)
end_date = datetime(2020, 11, 30)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[45:46,26]
        df1 = df1.rename(index={45: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)
    # Increment to the next date
    current_date += timedelta(days=1)  
###############################################################################
start_date = datetime(2020, 12, 1)
end_date = datetime(2021, 7, 31)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[45:46,26]
        df1 = df1.rename(index={45: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)

    # Increment to the next date
    current_date += timedelta(days=1)
#df.tail()
###############################################################################
start_date = datetime(2020, 8, 1)
end_date = datetime(2021, 12, 1)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[45:46,26]
        df1 = df1.rename(index={45: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)

    # Increment to the next date
    current_date += timedelta(days=1)
#df.tail()
"""
2ο έτος
"""

start_date = datetime(2021, 12, 2)
end_date = datetime(2022, 7, 31)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[50:51,26]
        df1 = df1.rename(index={50: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)

    # Increment to the next date
    current_date += timedelta(days=1)  


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Not to run  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""  

"""
Find where the layout of the excel changes
"""
# Find the indices where the value is equal to 0
indices_where_zero = df[df[0] == 0].index

print(indices_where_zero)  

"""
Drop all data from index 2021/12/20211202 and after, the layout has changed
"""
index_to_drop_from = '2021/12/20211202'
# Convert index to datetime to allow slicing
df.index = pd.to_datetime(df.index)
df = df[df.index < index_to_drop_from]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Until here
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
3ο 
"""
    
start_date = datetime(2022, 8, 1)
end_date = datetime(2022, 9, 8)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[50:51,26]
        df1 = df1.rename(index={50: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)

    # Increment to the next date
    current_date += timedelta(days=1)    
    
###############################################################################
start_date = datetime(2022, 8, 1)
end_date = datetime(2022, 9, 8)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[50:51,26]
        df1 = df1.rename(index={50: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)

    # Increment to the next date
    current_date += timedelta(days=1)      
###############################################################################
start_date = datetime(2022, 9, 9)
end_date = datetime(2022, 12, 31)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[50:51,26]
        df1 = df1.rename(index={50: date_str})
        df = pd.concat([df, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        non_existan_urls.append(url)

    # Increment to the next date
    current_date += timedelta(days=1)      
     
################################################################################    
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 8)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
      date_str = current_date.strftime(date_format)
      url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

      try:
          # Read the XLSX file into a pandas DataFrame
          df1 = pd.read_excel(url, sheet_name="System_Production").iloc[50:51,26]
          df1 = df1.rename(index={50: date_str})
          df = pd.concat([df, df1])
          #df = pd.concat([df, df1])
      except HTTPError as e:
          print(f"Error accessing URL: {url}")
          print(e)
          non_existan_urls.append(url)

      # Increment to the next date
      current_date += timedelta(days=1)    
df.tail()      
###############################################################################
start_date = datetime(2023, 1, 9)
end_date = datetime(2023, 7, 31)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
      date_str = current_date.strftime(date_format)
      url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

      try:
          # Read the XLSX file into a pandas DataFrame
          df1 = pd.read_excel(url, sheet_name="System_Production").iloc[50:51,26]
          df1 = df1.rename(index={50: date_str})
          df = pd.concat([df, df1])
          #df = pd.concat([df, df1])
      except HTTPError as e:
          print(f"Error accessing URL: {url}")
          print(e)
          non_existan_urls.append(url)

      # Increment to the next date
      current_date += timedelta(days=1)     
#df.tail()    
"""




Εδώ θα μπουν οι ημ/νιες αν χρειαστει να συμπληρώσουμε




"""    
    
    
    
"""
Work with the dataframe column name
"""
df.columns
df.rename(columns={0: 'DAILY LIGNITE PRODUCTION IN MWh'}, inplace=True)


# Modify the index format
df.index = df.index.str[8:]

df.head()
# Count unique index values
unique_index_count = df.index.nunique()

print("Number of unique index values:", unique_index_count)

df.info()

"""
Find the duplicate indexes
"""
duplicate_indexes = df.index[df.duplicated(keep=False)]
print(duplicate_indexes)
len(duplicate_indexes)


#Compare the duplicates
for index_label in duplicate_indexes:
    duplicate_rows = df[df.index == index_label]
    print(f"Duplicated indexes '{index_label}':")
    print(duplicate_rows)
    print("=" * 30)
    
#If they have the same values just drop the duplicates
df = df.reset_index()
df = df.drop_duplicates(subset='index', keep='first').set_index('index')

#We now have only the data with value = 0, its the data that we need to modify as the excel template has changed    
  

# Convert the index to datetime
df.index = pd.to_datetime(df.index, format='%Y/%m/%d')  
df.index.sort_values()
df.head()
df.info()

"""
Set index column name
"""
df.index.name = 'Date'

"""
For the non existant urls
"""    

date_pattern = r"/(\d{4}/\d{2}/\d{8})"

#Initialize an epty list to add there all the problematic urls
dates = []

for url in non_existan_urls:
    # searching string
    match_str = re.search(r'\d{4}\d{2}\d{2}', url)
    # computed date
    # feeding format
    res = datetime.strptime(match_str.group(), '%Y%m%d').date()
    dates.append(str(res))    
   
print("The problem dates are:");
for i in dates:
    print(i)
    
"""
Save the csv
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df.to_csv(f)
         
"""
Save the list with the dates that we did not include in the dataframe
"""
txt_path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/lignite_error_dates.txt"
with open(txt_path, 'w') as f:
    for index in dates:
        f.write(f"{index}\n")
        
   