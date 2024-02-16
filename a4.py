A4

import pandas as pd 
df = pd.read_csv('churn.csv') 
--------
print(df)
------
df.duplicated (keep=False).sum() 
-------
df['customerID'].duplicated (keep=False).sum() 
--------
df.isna.sum()
------
df['TotalCharges'].isna().sum()
-------
df['MonthlyCharges'].mean() 
-------
df[df['Dependents'].str.contains('1@#')] 
df ['Dependents']
-------
df.info()
--------
srs = df.agg({'MonthlyCharges': 'mean'}) 
df[ 'MonthlyCharges'] =df['MonthlyCharges'].fillna(value=srs) 
print(df['MonthlyCharges']) 
--------
"srs = dft.agg({'ffq': 'mean'})\nprint(srs)\n#df[df[ 'MonthlyCharges'].isn ull()]\n#print(srs)\ndft['ffq'] 
(same line)      = dft['ffq'].fillna(value=srs)"
--------
df.columns