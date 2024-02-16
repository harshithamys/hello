B2

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
-------
births_data=pd.read_csv('births.csv') 
-------
births_data 
-------
births_data.dtypes 
---------
births_data.info()
-----
births_data.index 
------
births_data.describe()
------
births_data.head(10)
------
births_data.tail(10)
------
births_data.isnull().sum()
------
births_data.isnull() 
------
births_data.pivot_table('births', index='year', columns='gender', aggfunc= 'sum')
-------
births_data.pivot_table('births', index='year', columns='gender', aggfunc= 'sum').plot()
------
male_births_2000=births_data[(births_data['year']==2000)&(births_data['gender']=='M')] 
total=male_births_2000['births'].sum() 
print(total) 
-----
births_data
-----
births_data['date'] = pd.to_datetime(births_data[['year', 'month', 'day'],errors='coerce')
births_data['date'] = pd.to_datetime (births_data['date']) 
births_data['day_of_week'] = births_data['date'].dt.day_name() 
births_data['decade'] = (births_data['year'] // 10) * 10
-----
avg_daily_by_day_and_decade= births_data.groupby(['day_of_week', 'decade'])['births'].mean.plot()
print(avg_daily_by_day_and_decade) 
-------                                                 
avg_daily_by_day_and_decade= births_data.groupby(['day_of_week', 'decade'])['births'].mean()
print(avg_daily_by_day_and_decade) 
--------
pd.set_option('display.max_rows',100) 
-------
avg_daily_by_day_and_decade= births_data.groupby('date')['births'].mean()
print(avg_daily_births_by_date)