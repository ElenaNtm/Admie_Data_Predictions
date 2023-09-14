# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:42:13 2023

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
Import the datasets
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).csv"
df = pd.read_csv(path)
df.head()

"""
Set Dates Column as index
"""
df.set_index('Date', inplace = True)

"""
Check for 0s in values
"""
# Find the indices where the value is equal to 0
indices_where_zero = df[df['DAILY LIGNITE PRODUCTION IN MWh'] == 0].index

print(indices_where_zero)  
#Drop the dashes(-) so as to automate the procedure of modification
indices_where_zero = [line.replace("-", "") for line in indices_where_zero]
#print(indices_where_zero[1])
#Modify the items so they are in the correct for for usage
modified_dates = []
for i in indices_where_zero :
    year = i[:4]
    month = i[4:6]
    day = i[6:]
    modified_date = f"{year}/{month}/{year}{month}{day}"
    modified_dates.append(modified_date)

print(modified_dates)

"""
Based on the above list drop those rows from the dataframe
"""
# Dropping rows based on indexes
df = df.drop(indices_where_zero)



"""
Save the dropped indexes to a list so as to change the format of the read data and complete the dataframe
"""
txt_path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/lignite_indices_where_zero.txt"
with open(txt_path, 'w') as f:
    for index in indices_where_zero:
        f.write(f"{index}\n")
        
"""
Modify the code from the original file to fill in the rows with zeros
"""
df_new = pd.DataFrame()
base_url = "https://www.admie.gr/sites/default/files/attached-files/type-file/"
for i in modified_dates:
    #date_str = i.strftime(date_format)
    url = f"{base_url}{i}_SystemRealizationSCADA_01.xls"
    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production").iloc[51:52,26]
        df1 = df1.rename(index={51: i})
        df_new = pd.concat([df_new, df1])
        #df = pd.concat([df, df1])
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        
df_new.tail()
df_new.info()
df_new.columns
"""
Concat the two dataframes
"""
df_new.rename(columns={0: 'DAILY LIGNITE PRODUCTION IN MWh'}, inplace=True)


# Modify the index format
df_new.index = df.index.str[8:]

# Convert the index to datetime
df_new.index = pd.to_datetime(df.index, format='%Y/%m/%d')  
df_new.index.sort_values()
#df.head()
#df.info()



"""
Save the modified dataframe in place of the dataframe we had in the beggining
"""
#output_path is the same as the path we had earlier to open the file
df.to_csv(path, index = True)

#save the file as excel 
excel_path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).xlsx"
df.to_excel(excel_path, index = True)
