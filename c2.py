C2

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
--------
nRowsRead = 1000 
df_automobile = pd.read_csv('Automobile_data.csv', delimiter=',' nrows=nRowsRead)
df_automobile_dataframeName = 'Automobile_data.csv' nRow, nCol = df_automobile.shape 
print (f'There are {nRow} rows and {nCol} columns') 
------
df_data = df_automobile.replace('?', np.NAN) 
df_data.isnull().sum() 
-------------
df_temp = df_automobile [df_automobile ['normalized-losses']!='?'] 
normalised_mean = df_temp['normalized-losses'].astype (int).mean()
df_automobile['normalized-losses']
    =df_automobile['normalized-losses'].replace('?',normalised_mean).astype(int)
df_temp = df_automobile [df_automobile ['price']!='?'] 
normalised_mean = df_temp['price'].astype (int).mean()
df_automobile['price']
    =df_automobile['price'].replace('?',normalised_mean).astype(int)
df_temp = df_automobile [df_automobile ['horsepower']!='?'] 
normalised_mean = df_temp['horsepower'].astype (int).mean()
df_automobile['horsepower']
    =df_automobile['horsepower'].replace('?',normalised_mean).astype(int)                                                                        
df_temp = df_automobile [df_automobile ['peak-rpm']!='?'] 
normalised_mean = df_temp['peak-rpm'].astype (int).mean()
df_automobile['peak-rpm']
    =df_automobile['peak-rpm'].replace('?',normalised_mean).astype(int) 
df_temp = df_automobile [df_automobile ['bore']!='?'] 
normalised_mean = df_temp['bore'].astype (float).mean()
df_automobile['bore']
    =df_automobile['bore'].replace('?',normalised_mean).astype(float)     
df_temp = df_automobile [df_automobile ['stroke']!='?'] 
normalised_mean = df_temp['stroke'].astype (float).mean()
df_automobile['stroke']
    =df_automobile['stroke'].replace('?',normalised_mean).astype(float) 
df_automobile['num-of-doors'] = df_automobile [ 'num-of-doors'].replace('?', 'four')
df_automobile.head() 
---------
plt.figure(figsize=(10, 6)) 
sns.countplot(data=df_automobile, x="num-of-doors", hue="fuel-type") 
plt.title("Distribution of Two and Four-Door Cars by Fuel Type") 
plt.show() 
--------
plt.figure(figsize=(10, 6)) 
sns.countplot(data=df_automobile, x="body-style", hue="fuel-type")
plt.title("Distribution of Cars by Body Style and Fuel Type") 
plt.show() 
------
plt.figure(figsize=(10, 6)) 
sns.countplot(data=df_automobile, x="body-style", hue="fuel-type", hue_order
plt.title("Total Number of Body Style Cars Categorized by Fuel Type")
plt.show() 
---------
plt.figure(figsize=(10, 8)) 
sns.boxplot(data=df_automobile, x="fuel-type", y="horsepower", hue="drive- wheels")
plt.title("Horsepower by Fuel Type and Drive Wheel Type") 
plt.show() 
-------