# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:04:38 2023

@author: Eleni


Ακόμη και εδώ έχουμε κάποια αρχεία τα οποία δεν μπορεί να τα διαβάσει, αν χρειαστεί θα το δούμε τότε
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
Loop the automated URL and import the excel files to the dataframe
"""
#For the urls that can not be read we will keep the date
not_found = []
# Initialize empty DataFrames and do all the jobs at once, so as to download only once the file
df_hydro = pd.DataFrame()
df_lignite = pd.DataFrame()
df_net_load = pd.DataFrame()
df_gas = pd.DataFrame()
df_res = pd.DataFrame()


base_url = "https://www.admie.gr/sites/default/files/attached-files/type-file/2020/03/"

  
"""
2018-2019
are non-leap years so:
"""
"""
2018
"""
months = [1,2,3,4,5,6,7,8,9,10,11,12]
days_in_month = {
    1: 31,  # January
    2: 28,  # February (non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31,  # December
}

for i in months:
   start_date = datetime(2018, i, 1)
   end_date = datetime(2018, i, days_in_month[i])
   date_format = "%Y%m%d"
   current_date = start_date

   while current_date <= end_date:
       date_str = current_date.strftime(date_format)
       url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

       try:
           # Read the XLSX file into a pandas DataFrame
           df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
           #Hydro                                                                     
           substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'TOTAL HYDRO'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date_str])
           df_hydro = pd.concat([df_hydro, row])
           df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date_str})
           
           #Lignite
           substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
          
           if not wanted_index:
               substring = 'TOTAL LIGNITE'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
           
           df_lignite = pd.concat([df_lignite, row])
           df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
           
           #Gas
           substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'TOTAL GAS'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date_str])
           
           df_gas = pd.concat([df_gas, row])
           df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
           
           
           #RES
           substring = 'TOTAL RES'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
          
           if not wanted_index:
               substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total RES'], index=[date_str])
           
           df_res = pd.concat([df_res, row])
           df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
           
           #Net Load
           substring = 'NET LOAD'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date_str])

           df_net_load = pd.concat([df_net_load, row])
           df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
       except HTTPError as e:
           print(f"Error accessing URL: {url}")
           print(e)
           not_found.append(current_date)

       # Increment to the next date
       current_date += timedelta(days=1) 
      
"""
2019 do the same as in 2018
We could enter both years in a double for, but it crushes
"""
months = [1,2,3,4,5,6,7,8,9,10,11,12]

for i in months:
   start_date = datetime(2019, i, 1)
   end_date = datetime(2019, i, days_in_month[i])
   date_format = "%Y%m%d"
   current_date = start_date

   while current_date <= end_date:
       date_str = current_date.strftime(date_format)
       url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

       try:
           # Read the XLSX file into a pandas DataFrame
           df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
           #Hydro                                                                     
           substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'TOTAL HYDRO'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date_str])
           df_hydro = pd.concat([df_hydro, row])
           df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date_str})
           
           #Lignite
           substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
          
           if not wanted_index:
               substring = 'TOTAL LIGNITE'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
           
           df_lignite = pd.concat([df_lignite, row])
           df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
           
           #Gas
           substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'TOTAL GAS'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date_str])
           
           df_gas = pd.concat([df_gas, row])
           df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
           
           
           #RES
           substring = 'TOTAL RES'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
          
           if not wanted_index:
               substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total RES'], index=[date_str])
           
           df_res = pd.concat([df_res, row])
           df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
           
           #Net Load
           substring = 'NET LOAD'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date_str])

           df_net_load = pd.concat([df_net_load, row])
           df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
       except HTTPError as e:
           print(f"Error accessing URL: {url}")
           print(e)
           not_found.append(current_date)

       # Increment to the next date
       current_date += timedelta(days=1)  

"""
2020 μας ενδιαφέρει μόνο μέχρι τον ιούλιο
Σπάει σε 2 καθώς ότι είναι από τον Μάιο και έπειτα έχουν άλλο url
"""
months=[1,2,3]
days_in_month = {
    1: 31,  # January
    2: 29,  # February (leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31,  # December
}
for i in months:
   start_date = datetime(2020, i, 1)
   end_date = datetime(2020, i, days_in_month[i] )
   date_format = "%Y%m%d"
   current_date = start_date

   while current_date <= end_date:
       date_str = current_date.strftime(date_format)
       url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

       try:
           # Read the XLSX file into a pandas DataFrame
           df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
           #Hydro                                                                     
           substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'TOTAL HYDRO'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date_str])
           df_hydro = pd.concat([df_hydro, row])
           df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date_str})
           
           #Lignite
           substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
          
           if not wanted_index:
               substring = 'TOTAL LIGNITE'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
           
           df_lignite = pd.concat([df_lignite, row])
           df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
           
           #Gas
           substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'TOTAL GAS'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date_str])
           
           df_gas = pd.concat([df_gas, row])
           df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
           
           
           #RES
           substring = 'TOTAL RES'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total RES'], index=[date_str])
           
           df_res = pd.concat([df_res, row])
           df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
           
           #Net Load
           substring = 'NET LOAD'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date_str])
          
           df_net_load = pd.concat([df_net_load, row])
           df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
       except HTTPError as e:
           print(f"Error accessing URL: {url}")
           print(e)
           not_found.append(current_date)

       # Increment to the next date
       current_date += timedelta(days=1) 
base_url = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/04/'
start_date = datetime(2020, 3, 27)
end_date = datetime(2020, 3, 31)
date_format = "%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
        #Hydro                                                                     
        substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
        
        if not wanted_index:
            substring = 'TOTAL HYDRO'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date_str])
        df_hydro = pd.concat([df_hydro, row])
        df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date_str})
        
        #Lignite
        substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
       
        if not wanted_index:
            substring = 'TOTAL LIGNITE'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
        
        df_lignite = pd.concat([df_lignite, row])
        df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
        
        #Gas
        substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
        
        if not wanted_index:
            substring = 'TOTAL GAS'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date_str])
        
        df_gas = pd.concat([df_gas, row])
        df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
        
        
        #RES
        substring = 'TOTAL RES'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
        
        if not wanted_index:
            substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total RES'], index=[date_str])
        
        df_res = pd.concat([df_res, row])
        df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
        
        #Net Load
        substring = 'NET LOAD'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
        
        if not wanted_index:
            substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date_str])
       
        df_net_load = pd.concat([df_net_load, row])
        df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        not_found.append(current_date)

    # Increment to the next date
    current_date += timedelta(days=1) 
month = [4,5,6,7]  
base_url = "https://www.admie.gr/sites/default/files/attached-files/type-file/2020/07/"
for i in month:
   start_date = datetime(2020, 7, 29)
   end_date = datetime(2020, 7, 30)
   date_format = "%Y%m%d"
   current_date = start_date

   while current_date <= end_date:
       date_str = current_date.strftime(date_format)
       url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

       try:
           # Read the XLSX file into a pandas DataFrame
           df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
           #Hydro                                                                     
           substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'TOTAL HYDRO'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date_str])
           df_hydro = pd.concat([df_hydro, row])
           df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date_str})
           
           #Lignite
           substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
          
           if not wanted_index:
               substring = 'TOTAL LIGNITE'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
           
           df_lignite = pd.concat([df_lignite, row])
           df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
           
           #Gas
           substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'TOTAL GAS'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date_str])
           
           df_gas = pd.concat([df_gas, row])
           df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
           
           
           #RES
           substring = 'TOTAL RES'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total RES'], index=[date_str])
           
           df_res = pd.concat([df_res, row])
           df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
           
           #Net Load
           substring = 'NET LOAD'
           filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
           wanted_index = filtered.index.tolist()
           
           if not wanted_index:
               substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
               filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
               wanted_index = filtered.index.tolist()
           
           value = df1.iloc[wanted_index[len(wanted_index)-1],26]
           row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date_str])
           
           df_net_load = pd.concat([df_net_load, row])
           df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date_str}) 
       except HTTPError as e:
           print(f"Error accessing URL: {url}")
           print(e)
           not_found.append(current_date)

       # Increment to the next date
       current_date += timedelta(days=1)   


for i in not_found:
    print(i)       
"""
Drop duplicate indexes
"""
#RES
df_res['index'] = df_res.index
df_res = df_res.drop_duplicates(subset='index')
df_res.drop(['index'], axis = 1, inplace = True)

#HYDRO
df_hydro['index'] = df_hydro.index
df_hydro = df_hydro.drop_duplicates(subset='index')
df_hydro.drop(['index'], axis = 1, inplace = True)

#LIGNITE
df_lignite['index'] = df_lignite.index
df_lignite = df_lignite.drop_duplicates(subset='index')
df_lignite.drop(['index'], axis = 1, inplace = True)

#NET LOAD
df_net_load['index'] = df_net_load.index
df_net_load = df_net_load.drop_duplicates(subset='index')
df_net_load.drop(['index'], axis = 1, inplace = True)

#GAS
df_gas['index'] = df_gas.index
df_gas = df_gas.drop_duplicates(subset='index')
df_gas.drop(['index'], axis = 1, inplace = True)

not_found = list(set(not_found))


"""
Work on the dataframes indexes and column names
"""

# Convert the index to datetime
df_res.index = pd.to_datetime(df_res.index, format='%Y/%m/%d')  
df_lignite.index = pd.to_datetime(df_lignite.index, format='%Y/%m/%d') 
df_net_load.index = pd.to_datetime(df_net_load.index, format='%Y/%m/%d')
df_hydro.index = pd.to_datetime(df_hydro.index, format='%Y/%m/%d')  
df_gas.index = pd.to_datetime(df_gas.index, format='%Y/%m/%d') 


"""
Set index column name
"""
df_res.index.name = 'Date'
df_net_load.index.name = 'Date'
df_lignite.index.name = 'Date'
df_hydro.index.name = 'Date'
df_gas.index.name = 'Date'
"""
Missing Data
"""
#Join all to one dataframe to see for missing data
df = pd.DataFrame()
df = df_gas.join(df_res,on = 'Date', how = 'outer')
df = df.join(df_hydro,on = 'Date', how = 'outer')
df = df.join(df_lignite,on = 'Date', how = 'outer')
df = df.join(df_net_load, on = 'Date',how = 'outer')
df.reset_index(drop=False, inplace=True)
df.head()
total = df.isnull().sum().sort_values(ascending=False)
percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(10)
df.tail(20)
df_net_load.tail(20)
"""
Upload the files with the info from August 2020 to today
"""
#path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Hydro_Production.csv"
#df_new_ = pd.read_csv(path, index_col='Date')
#df_new.index = pd.to_datetime(df_new.index, format='%Y/%m/%d')  

"""
Concat the two dataframes
"""
#df = pd.concat([df,df_new])

#df.index.sort_values()

"""
Save the csv and the list to separate file
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_Hydro_Production.csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_hydro.to_csv(f)

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_Lignite_Production.csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_lignite.to_csv(f)         

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_Gas_Production.csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_gas.to_csv(f)
  
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_RES_Production.csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_res.to_csv(f)  
  
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_NET_LOAD_Production.csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_net_load.to_csv(f)  

file = open('old_not_found.txt','w')
for item in not_found:
    file.write(item+"\n")
file.close()   

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/old_not_found.txt"
with open(path, 'w') as fp:
    for item in not_found:
        # write each item on a new line
        fp.write("%s\n" % item)