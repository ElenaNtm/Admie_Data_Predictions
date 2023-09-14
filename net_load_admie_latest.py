# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:53:24 2023

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
#import re

"""
Loop the urls
"""
# Initialize an empty DataFrame
df = pd.DataFrame()
df_not_found = pd.DataFrame()
"""
Οι ημ/νιες από 01/08/2020 δεν έχουν κάποιο θέμα εκτός από τη τελευταία μέρα του μήνα το οποίο θα το λύσουμε
θα το σπάσουμε ανά χρόνο γιατί κρασάρει η διαδικασία αλλιώς
"""
base_url = "https://www.admie.gr/sites/default/files/attached-files/type-file/"
"""
Έτος 2020- Αύγουστος μέχρι Δεκέμβρης
"""

#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2020, 8, 1)
end_date = datetime(2020, 12, 31)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
        #Search for the line we are interested in, it might contain the string TOTAL LIGNITE or ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ                                                                     
        substring = 'NET LOAD'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
        
        #Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
        if not wanted_index:
            substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
        #row.transpose()

        df = pd.concat([df, row])
        df = df.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
    except HTTPError as e:
        print(f"Error accessing URL: {url}")
        print(e)
        

    # Increment to the next date
    current_date += timedelta(days=1)

"""
2020 Not found urls
"""
url8 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/09/20200831_SystemRealizationSCADA_01.xls'
url9 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/10/20200930_SystemRealizationSCADA_01.xls'
url10 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/11/20201031_SystemRealizationSCADA_01.xls'
url11 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2020/12/20201130_SystemRealizationSCADA_01.xls'
url12 = 'https://www.admie.gr/sites/default/files/attached-files/type-file/2021/01/20201231_SystemRealizationSCADA_01.xls'

#Aug
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2020/09/20210831'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2020/09/20210831'})  

#Sep
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2020/10/20210930'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2020/10/20210930'})  

#Oct
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2020/11/20201031'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2020/11/20201031'})  

#Nov
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2020/12/20201130'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2020/12/20201130'})  

#Dec
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/01/20201231'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/01/20201231'})  


"""
Έτος 2021
"""    

#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
        #Search for the line we are interested in, it might contain the string TOTAL LIGNITE or ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ                                                                     
        substring = 'NET LOAD'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
        
        #Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
        if not wanted_index:
            substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
        #row.transpose()

        df = pd.concat([df, row])
        df = df.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
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

#Jan
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/02/20210131'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/02/20210131'})  

#Feb
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/03/20210228'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/03/20210228'})  

#Mar
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/04/20210331'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/04/20210331'})  

#Apr
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/05/20210430'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/05/20210430'})  

#May
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/06/20210531'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/06/20210531'})  

#June
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/07/20210630'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/07/20210630'})  

#July
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/08/20210731'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/08/20210731'})  


#Aug
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/09/20210831'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/09/20210831'})  

#Sep
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/10/20210930'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/10/20210930'})  

#Oct
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/11/20211031'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/11/20211031'})  

#Nov
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2021/12/20211130'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2021/12/20211130'})  

#Dec
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/01/20211231'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/01/20211231'})  


 
"""
Έτος 2022
"""    

#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
        #Search for the line we are interested in, it might contain the string TOTAL LIGNITE or ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ                                                                     
        substring = 'NET LOAD'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
        
        #Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
        if not wanted_index:
            substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
        #row.transpose()

        df = pd.concat([df, row])
        df = df.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
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

#Jan
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/02/20220131'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/02/20220131'})  

#Feb
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/03/20220228'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/03/20220228'})  

#Mar
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/04/20220331'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/04/20220331'})  

#Apr
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/05/20220430'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/05/20220430'})  

#May
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/06/20220531'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/06/20220531'})  

#June
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/07/20220630'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/07/20220630'})  

#July
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/08/20220731'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/08/20220731'})  



#Aug
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/09/20220831'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/09/20220831'})  

#Sep
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/10/20220930'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/10/20220930'})  

#Oct
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/11/20221031'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/11/20221031'})  

#Nov
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2022/12/20221130'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2022/12/20221130'})  

#Dec
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2023/01/20221231'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2023/01/20221231'})  


 
"""
Έτος 2023
"""    

#Manualy change the dates because if loaded all the system will crush
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 8, 25)
date_format = "%Y/%m/%Y%m%d"
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    url = f"{base_url}{date_str}_SystemRealizationSCADA_01.xls"

    try:
        # Read the XLSX file into a pandas DataFrame
        df1 = pd.read_excel(url, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
        #Search for the line we are interested in, it might contain the string TOTAL LIGNITE or ΣΥΝΟΛΟ ΛΙΓΝΙΤΙΚΩΝ                                                                     
        substring = 'NET LOAD'
        filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
        wanted_index = filtered.index.tolist()
        
        #Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
        if not wanted_index:
            substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
            filtered = df1[df1.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
            wanted_index = filtered.index.tolist()
        
        value = df1.iloc[wanted_index[len(wanted_index)-1],26]
        row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=[date_str])
        #row.transpose()

        df = pd.concat([df, row])
        df = df.rename(index={wanted_index[len(wanted_index)-1]: date_str})  
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

#Jan
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2023/02/20230131'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2023/02/20230131'})  

#Feb
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2023/03/20230228'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2023/03/20230228'})  

#Mar
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2023/04/20230331'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2023/04/20230331'})  

#Apr
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2023/05/20230430'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2023/05/20230430'})  

#May
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2023/06/20230531'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2023/06/20230531'})  

#June
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2023/07/20230630'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2023/07/20230630'})  

#July
df2 = pd.read_excel(url8, sheet_name="System_Production", converters={'(ΣΤΟΙΧΕΙΑ SCADA ΜΗ-ΠΙΣΤΟΠΟΙΗΜΕΝΑ)':str})
substring = 'NET LOAD'
filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
wanted_index = filtered.index.tolist()

#Check if we have the TOTAL LIGNITE in the dataframe, if not we procede searching for the Greek version- the list wanted_index will be empty
if not wanted_index:
    substring = 'ΚΑΘΑΡΟ ΦΟΡΤΙΟ'
    filtered = df2[df2.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    wanted_index = filtered.index.tolist()

value = df2.iloc[wanted_index[len(wanted_index)-1],26]
row = pd.DataFrame([[value]], columns=['Total Lignite in MWh'], index=['2023/08/20230731'])
df_not_found = pd.concat([df_not_found , row])
df_not_found = df_not_found.rename(index={wanted_index[len(wanted_index)-1]: '2023/08/20230731'})  


"""
Concat the two dataframes
"""
df = pd.concat([df,df_not_found])


"""
Work on the dataframe indexes
"""
# Modify the index format
df.index = df.index.str[8:]

df.head()

# Convert the index to datetime
df.index = pd.to_datetime(df.index, format='%Y/%m/%d')  
df.index.sort_values()
df.head()
df.info()

"""
Set index column name
"""
df.index.name = 'Date'
df = df.rename(columns={'Total Lignite in MWh':'Net Load'})
df.head()

"""
Save the csv
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Daily_Net_Load.csv"
with open(path, 'w', encoding = 'utf-8-sig') as f:
  df.to_csv(f)
         
