import pandas as pd
df=pd.read_csv('Book1.csv')
print(df)

""" 
print(df.head(3))
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
"""

print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))
print(df.mode(numeric_only=True))

print(df.std(numeric_only=True))
print(df.var(numeric_only=True))