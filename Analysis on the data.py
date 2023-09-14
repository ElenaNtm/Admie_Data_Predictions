# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:50:13 2023

@author: Eleni
"""

"""
Load Libraries
"""
import pandas as pd 
import numpy as np
import math
import operator 
from datetime import datetime
import seaborn as sns
from datetime import datetime, timedelta
import math
import operator 
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from pandas.plotting import scatter_matrix
from pandas.plotting import autocorrelation_plot
from pandas.plotting import bootstrap_plot

"""
Load Data
"""
path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Daily_Net_Load.csv"
df_net_load = pd.read_csv(path, index_col='Date')

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Gas_Production.csv"
df_gas = pd.read_csv(path, index_col='Date')

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/RES_Production.csv"
df_res = pd.read_csv(path, index_col='Date')

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Hydro_Production.csv"
df_hydro = pd.read_csv(path, index_col='Date')

path = "C:/Users/Eleni/Desktop/Χρυσοχόου/created data/Lignite_Production(MWh).csv"
df_lignite = pd.read_csv(path, index_col='Date')

df = pd.DataFrame()


df_net_load.index = pd.to_datetime(df_net_load.index).strftime('%Y/%m/%d')
for i in range(len(df_net_load)) :
    df_net_load.at[i, 'Date'] = df_net_load.at[i, 'Date'].replace("-","/")
"""
Περνάμε όλα τα παραπάνω σε ένα dataframe
"""
df = df_gas.join(df_res)
df = df.join(df_hydro)
df = df.join(df_lignite)
df = df.join(df_net_load)
df.reset_index(drop=False, inplace=True)

for i in range(len(df)) :
    df.at[i, 'Date'] = df.at[i, 'Date'].replace("-","/")
df.sort_index(inplace=True) 
df.head()

"""
Missing Values
"""
total = df.isnull().sum().sort_values(ascending=False)
percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(10)

"""
Find dates of missing values
"""
dates_with_missing_values = df[df.isnull().any(axis=1)].index
#dates_with_missing_values = sorted(dates_with_missing_values)
dates_with_missing_values = list(set(dates_with_missing_values))
for i in dates_with_missing_values:
    print(i)
len(dates_with_missing_values)
drop = '2023/09/30'
df = df.drop(drop)

"""
Drop the duplicates
"""
df = df.drop_duplicates()
df.head()
df.info()
df.describe()

"""
Corelation Matrix
"""
# prints data that will be plotted columns shown here are selected by corr() since they are ideal for the plot
print(df.corr())
# plotting correlation heatmap
dataplot = sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)

"""
Plotting the columns
"""
sns.displot(df['Total Gas'],kde=True,color='yellow',height=5,aspect=1) 
sns.displot(df['Total RES'],kde=True,color='green',height=5,aspect=1) 
sns.displot(df['Total Lignite in MWh'],kde=True,color='red',height=5,aspect=1) 
sns.displot(df['Total Hydro'],kde=True,color='blue',height=5,aspect=1) 
#Combined
df.plot.kde();
"""
Plot the columns bassed on the date
"""
#GAS
plt.scatter(df.index, df['Total Gas'],marker='o', s = 5, color = 'red')
plt.xlabel('Date')
plt.ylabel('Total Gas')
plt.title('Values of Gas Over Time')
plt.xticks(rotation=45)  
plt.show()

#HYDRO
plt.scatter(df.index, df['Total Hydro'],marker='o', s = 5)
plt.xlabel('Date')
plt.ylabel('Total Hydro')
plt.title('Values of Hydro Over Time')
plt.xticks(rotation=45)  
plt.show()

#RES
plt.scatter(df.index, df['Total RES'],marker='o', s = 5, color = 'green')
plt.xlabel('Date')
plt.ylabel('Total RES')
plt.title('Values of RES Over Time')
plt.xticks(rotation=45)  
plt.show()

#LIGNITE
plt.scatter(df.index, df['Total Lignite in MWh'],marker='o', s = 5, color = 'grey')
plt.xlabel('Date')
plt.ylabel('Total Lignite in MWh')
plt.title('Values of Lignite Over Time')
plt.xticks(rotation=45)  
plt.show()

#NET LOAD
plt.scatter(df.index, df['Total Net Load'],marker='o', s = 5, color = 'grey')
plt.xlabel('Date')
plt.ylabel('Total Net Load')
plt.title('Net Load Over Time')
plt.xticks(rotation=45)  
plt.show()

#Combine them all
plt.scatter(df.index, df['Total Net Load'],marker='o', s = 5, color = 'purple', label = 'Net Load')
plt.scatter(df.index, df['Total Lignite in MWh'],marker='o', s = 1, color = 'grey', label = 'Lignite')
plt.scatter(df.index, df['Total RES'],marker='o', s = 1, color = 'green', label = 'RES')
plt.scatter(df.index, df['Total Hydro'],marker='o', s = 1, label = 'Hydro')
plt.scatter(df.index, df['Total Gas'],marker='o', s = 1, color = 'red', label = "Gas")
plt.xlabel('Date')
plt.xticks(rotation=45)  
plt.show()






"""
Plot area
"""
df.plot.area();
df.plot.area(stacked=False);

"""
Α matrix of scatter plots used to visualize bivariate relationships between combinations of variables.
"""
scatter_matrix(df, alpha=0.2, figsize=(8, 8), diagonal="kde");

"""
Lag plot 
"""

plt.figure();

spacing = np.linspace(-99 * np.pi, 99 * np.pi, num=1000)

data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(spacing))

lag_plot(df['Total Hydro']);
lag_plot(df['Total Gas'])
lag_plot(df['Total RES'])


"""
Autovorrelation plot
To check for randomness in the timeseries
If time series is random, such autocorrelations should be near zero for any and all time-lag separations. If time series is non-random then one or more of the autocorrelations will be significantly non-zero. The horizontal lines displayed in the plot correspond to 95% and 99% confidence bands. The dashed line is 99% confidence band.
"""

plt.figure();

spacing = np.linspace(-9 * np.pi, 9 * np.pi, num=1000)


autocorrelation_plot(df['Total RES']);
autocorrelation_plot(df['Total Hydro']);
autocorrelation_plot(df['Total Gas']);
autocorrelation_plot(df['Total Lignite in MWh']);
autocorrelation_plot(df['Total Net Load']);


"""
Bootstrap plot
"""
bootstrap_plot(df_net_load['Total Net Load'], size=50, samples=500, color="grey");
bootstrap_plot(df_gas['Total Gas'], size=50, samples=500, color="grey");
bootstrap_plot(df_gas['Total Hydro'], size=50, samples=500, color="grey");
bootstrap_plot(df_gas['Total RES'], size=50, samples=500, color="grey");


df_net_load.info()



