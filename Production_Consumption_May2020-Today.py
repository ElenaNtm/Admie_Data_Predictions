# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:01:16 2023

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
#import re
#from urllib.parse import urlparse
"""
Loop the urls
"""
# Initialize an empty DataFrame
#df = pd.DataFrame()
#df_not_found = pd.DataFrame()
df_hydro = pd.DataFrame()
df_lignite = pd.DataFrame()
df_net_load = pd.DataFrame()
df_gas = pd.DataFrame()
df_res = pd.DataFrame()

"""
Οι ημ/νιες από 01/08/2020 δεν έχουν κάποιο θέμα εκτός από τη τελευταία μέρα του μήνα το οποίο θα το λύσουμε
θα το σπάσουμε ανά χρόνο γιατί κρασάρει η διαδικασία αλλιώς
"""
base_url = "https://www.admie.gr/sites/default/files/attached-files/type-file/"
"""
Έτος 2020- Ιούνιος μέχρι Δεκέμβρης
"""

#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2020, 12, 23)
end_date = datetime(2020, 12, 31)
date_format = "%Y/%m/%Y%m%d"
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
        #print(e)
        

    # Increment to the next date
    current_date += timedelta(days=1)

"""
2020 Not found urls
"""
url6 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/07/20200630_SystemRealizationSCADA_01.xls'
url7 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/08/20200731_SystemRealizationSCADA_01.xls'
url8 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/09/20200831_SystemRealizationSCADA_01.xls'
url9 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/10/20200930_SystemRealizationSCADA_01.xls'
url10 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/11/20201031_SystemRealizationSCADA_01.xls'
url11 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/12/20201130_SystemRealizationSCADA_01.xls'
url12 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2021/01/20201231_SystemRealizationSCADA_01.xls'
url = [url6,url7,url8,url9,url10,url11,url12]
date = {url6: '2020/07/20200630', #June
        url7: '2020/07/20200731', #July
        url8: '2020/07/20200831', #August
        url9: '2020/07/20200930', #September
        url10: '2020/07/20201031', #Octomber
        url11: '2020/07/20201130', #November
        url12: '2020/07/20201031', #December
}

for i in url:
    df2 = pd.read_excel(i, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
    #Hydro                                                                     
    substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL HYDRO'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date[i]])
    df_hydro = pd.concat([df_hydro, row])
    df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date[i]})
    
    #Lignite
    substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL LIGNITE'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date[i]])

    df_lignite = pd.concat([df_lignite, row])
    df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

    #Gas
    substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL GAS'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date[i]])

    df_gas = pd.concat([df_gas, row])
    df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

    #RES
    substring = 'TOTAL RES'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total RES'], index=[date[i]])

    df_res = pd.concat([df_res, row])
    df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date[i]})  

    #Net Load
    substring = 'NET LOAD'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date[i]])

    df_net_load = pd.concat([df_net_load, row])
    df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

"""
Έτος 2021
"""    
#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2021, 11, 1)
end_date = datetime(2021, 12, 31)
date_format = "%Y/%m/%Y%m%d"
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
     

    # Increment to the next date
    current_date += timedelta(days=1)
  
"""
Προβληματικά url γίνεται η διαδικασία στο χέρι γιατί δεν αναγνωρίζει τους χαρακτήρες 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ' και 'TOTAL LIGNITE'
"""

url1 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/02/20210131_SystemRealizationSCADA_01.xls"
url2 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/03/20210228_SystemRealizationSCADA_01.xls"
url3 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/04/20210331_SystemRealizationSCADA_01.xls"
url4 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/05/20210430_SystemRealizationSCADA_01.xls"
url5 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/06/20210531_SystemRealizationSCADA_01.xls"
url6 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/07/20210630_SystemRealizationSCADA_01.xls"
url7 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/08/20210731_SystemRealizationSCADA_01.xls"
url8 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/09/20210831_SystemRealizationSCADA_01.xls"
url9 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/10/20210930_SystemRealizationSCADA_01.xls"
url10 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/11/20211031_SystemRealizationSCADA_01.xls"
url11 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2021/12/20211130_SystemRealizationSCADA_01.xls"
url12 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/01/20211231_SystemRealizationSCADA_01.xls"

url = [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10, url11, url12]
date = {url1: '2020/07/20210131', #June
        url2: '2020/07/20210228', #July
        url3: '2020/07/20210331', #August
        url4: '2020/07/20210430', #September
        url5: '2020/07/20210531', #Octomber
        url6: '2020/07/20210630', #June
        url7: '2020/07/20210731', #July
        url8: '2020/07/20210831', #August
        url9: '2020/07/20210930', #September
        url10: '2020/07/20211031', #Octomber
        url11: '2020/07/20211130', #November
        url12: '2020/07/20211031' #December
}

for i in url:
    df2 = pd.read_excel(i, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
    #Hydro                                                                     
    substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL HYDRO'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date[i]])
    df_hydro = pd.concat([df_hydro, row])
    df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date[i]})
    
    #Lignite
    substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL LIGNITE'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date[i]])

    df_lignite = pd.concat([df_lignite, row])
    df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

    #Gas
    substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL GAS'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date[i]])

    df_gas = pd.concat([df_gas, row])
    df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

    #RES
    substring = 'TOTAL RES'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total RES'], index=[date[i]])

    df_res = pd.concat([df_res, row])
    df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date[i]})  

    #Net Load
    substring = 'NET LOAD'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date[i]])

    df_net_load = pd.concat([df_net_load, row])
    df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

"""
Έτος 2022
"""    

#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2022, 11, 1)
end_date = datetime(2022, 12, 31)
date_format = "%Y/%m/%Y%m%d"
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
     

    # Increment to the next date
    current_date += timedelta(days=1)

"""
Προβληματικά url γίνεται η διαδικασία στο χέρι γιατί δεν αναγνωρίζει τους χαρακτήρες 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ' και 'TOTAL LIGNITE'
"""

url1 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/02/20220131_SystemRealizationSCADA_01.xls"
url2 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/03/20220228_SystemRealizationSCADA_01.xls"
url3 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/04/20220331_SystemRealizationSCADA_01.xls"
url4 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/05/20220430_SystemRealizationSCADA_01.xls"
url5 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/06/20220531_SystemRealizationSCADA_01.xls"
url6 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/07/20220630_SystemRealizationSCADA_01.xls"
url7 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/08/20220731_SystemRealizationSCADA_01.xls"
url8 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/09/20220831_SystemRealizationSCADA_01.xls"
url9 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/10/20220930_SystemRealizationSCADA_01.xls"
url10 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/11/20221031_SystemRealizationSCADA_01.xls"
url11 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/12/20221130_SystemRealizationSCADA_01.xls"
url12 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/01/20221231_SystemRealizationSCADA_01.xls"
url = [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10, url11, url12]
date = {url1: '2020/07/20220131', #June
        url2: '2020/07/20220228', #July
        url3: '2020/07/20220331', #August
        url4: '2020/07/20220430', #September
        url5: '2020/07/20220531', #Octomber
        url6: '2020/07/20220630', #June
        url7: '2020/07/20220731', #July
        url8: '2020/07/20220831', #August
        url9: '2020/07/20220930', #September
        url10: '2020/07/20221031', #Octomber
        url11: '2020/07/20221130', #November
        url12: '2020/07/20221031' #December
}

for i in url:
    df2 = pd.read_excel(i, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
    #Hydro                                                                     
    substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL HYDRO'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date[i]])
    df_hydro = pd.concat([df_hydro, row])
    df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date[i]})
    
    #Lignite
    substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL LIGNITE'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date[i]])

    df_lignite = pd.concat([df_lignite, row])
    df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

    #Gas
    substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL GAS'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date[i]])

    df_gas = pd.concat([df_gas, row])
    df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

    #RES
    substring = 'TOTAL RES'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total RES'], index=[date[i]])

    df_res = pd.concat([df_res, row])
    df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date[i]})  

    #Net Load
    substring = 'NET LOAD'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date[i]])

    df_net_load = pd.concat([df_net_load, row])
    df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 



"""
Έτος 2023
"""    
#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2023, 8, 23)
end_date = datetime(2023, 8, 31)
date_format = "%Y/%m/%Y%m%d"
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
     

    # Increment to the next date
    current_date += timedelta(days=1)


"""
Προβληματικά url γίνεται η διαδικασία στο χέρι γιατί δεν αναγνωρίζει τους χαρακτήρες 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ' και 'TOTAL LIGNITE'
"""

url1 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/02/20230131_SystemRealizationSCADA_01.xls"
url2 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/03/20230228_SystemRealizationSCADA_01.xls"
url3 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/04/20230331_SystemRealizationSCADA_01.xls"
url4 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/05/20230430_SystemRealizationSCADA_01.xls"
url5 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/06/20230531_SystemRealizationSCADA_01.xls"
url6 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/07/20230630_SystemRealizationSCADA_01.xls"
url7 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/08/20230731_SystemRealizationSCADA_01.xls"
url8 = "https://www.admie.gr/sites/default/files/attached-files/type-file/2023/09/20230831_SystemRealizationSCADA_01.xls"
url = [url1, url2, url3, url4, url5, url6, url7, url8]
date = {url1: '2020/07/20230131', #June
        url2: '2020/07/20230228', #July
        url3: '2020/07/20230331', #August
        url4: '2020/07/20230430', #September
        url5: '2020/07/20230531', #Octomber
        url6: '2020/07/20230630', #June
        url7: '2020/07/20230731', #July
        url8: '2020/07/20230831', #August
        }

for i in url:
    df2 = pd.read_excel(i, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
    #Hydro                                                                     
    substring = 'ΣΥΝΟΛΟ ΥΔΡΟΗΛΕΚΤΡΙΚΩΝ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL HYDRO'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Hydro'], index=[date[i]])
    df_hydro = pd.concat([df_hydro, row])
    df_hydro = df_hydro.rename(index={wanted_index[len(wanted_index)-1]: date[i]})
    
    #Lignite
    substring = 'ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL LIGNITE'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date[i]])

    df_lignite = pd.concat([df_lignite, row])
    df_lignite = df_lignite.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

    #Gas
    substring = 'ΣΥΝΟΛΟ Φ. ΑΕΡΙΟΥ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'TOTAL GAS'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Gas'], index=[date[i]])

    df_gas = pd.concat([df_gas, row])
    df_gas = df_gas.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

    #RES
    substring = 'TOTAL RES'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'ΣΥΝΟΛΟ ΑΙΟΛΙΚΩΝ'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total RES'], index=[date[i]])

    df_res = pd.concat([df_res, row])
    df_res = df_res.rename(index={wanted_index[len(wanted_index)-1]: date[i]})  

    #Net Load
    substring = 'NET LOAD'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

    if not wanted_index:
        substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
        filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()

    value = df2.iloc[wanted_index[len(wanted_index)-1],26]
    row = pd.DataFrame([[value]], columns=['Total Net Load'], index=[date[i]])

    df_net_load = pd.concat([df_net_load, row])
    df_net_load = df_net_load.rename(index={wanted_index[len(wanted_index)-1]: date[i]}) 

df_net_load.tail(1)
"""
Drop any duplicate values from the dataframes
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


"""
Work on the dataframe indexes
"""
# Modify the index format
df_gas.index = df_gas.index.str[8:]
df_hydro.index = df_hydro.index.str[8:]
df_lignite.index = df_lignite.index.str[8:]
df_net_load.index = df_net_load.index.str[8:]
df_res.index = df_res.index.str[8:]

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
Look for missing values and run those dates again
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
Concat and save the dfs
"""

"""
Save the csvs
Concated because the code would crush all the time so I saved part of the data in the beggining
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).csv"
df_old = pd.read_csv(path, index_col='Date')
df_lignite = pd.concat([df_lignite, df_old])
df_lignite.index = pd.to_datetime(df_lignite.index)
df_lignite.index = df_lignite.index.strftime('%Y/%m/%d')
#df_lignite.index = df_lignite.index.date
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_lignite.to_csv(f)

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Hydro_Production.csv"
df_old = pd.read_csv(path, index_col='Date')
df_hydro = pd.concat([df_hydro, df_old])
df_hydro.index = pd.to_datetime(df_hydro.index)
df_hydro.index = df_hydro.index.strftime('%Y/%m/%d')
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_hydro.to_csv(f)
                  
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/RES_Production.csv"
df_old = pd.read_csv(path, index_col='Date')
df_res = pd.concat([df_res, df_old])
df_res.index = pd.to_datetime(df_res.index)
df_res.index = df_res.index.strftime('%Y/%m/%d')
df_res.head()
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_res.to_csv(f)
                  
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Gas_Production.csv"
df_old = pd.read_csv(path, index_col='Date')
df_gas = pd.concat([df_gas, df_old])
df_gas.index = pd.to_datetime(df_gas.index)
df_gas.index = df_gas.index.strftime('%Y/%m/%d')
df_gas.head()
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_gas.to_csv(f)

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Daily_Net_Load.csv"
df_old = pd.read_csv(path, index_col='Date')
df_net_load = pd.concat([df_net_load, df_old])
df_gas.index = pd.to_datetime(df_gas.index)
df_gas.index = df_gas.index.strftime('%Y/%m/%d')
df_gas.head()
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df_net_load.to_csv(f)
                                      