B1

import numpy as np 
import pandas as pd 
-----
import pandas as pd 
import matplotlib.pyplot as plt 
data = pd.read_csv('Fremont Bridge.csv'(copy path), index_col='Date', parse_dates=True)
data.columns = ['Total', 'East', 'West']  
data.head() 
------
print(data.dropna().describe()) 
data.plot() 
plt.ylabel('Hourly Bicycle Count'); 
------
print(data.dropna().info()) 
-----
weekly=data.resample('W').sum() 
weekly.plot(style=[':', '--','-'])
plt.ylabel('Weekly bicycle count'); 
------
by_weekday=data.groupby(data.index.dayofweek).mean() 
by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'] 
by_weekday.plot(style=[':','--','-']); 
------
import numpy as np 
weekend_array = np.where(data.index.weekday < 5, 'Weekday', 'Weekend') 
by_time = data.groupby([weekend_array, data.index.time]).mean() 
by_time.loc['Weekday'].plot(title='Weekdays', style=[':','--','-']) 
by_time.loc['Weekend'].plot(title='Weekends', style=[':','--','-'])