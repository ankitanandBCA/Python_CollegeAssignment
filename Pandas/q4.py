import pandas as pd
d=pd.Series([-2,10,12,14,16,18,20,200])

q1=d.quantile(0.25)
q3=d.quantile(0.75)

iqr=q3-q1

lb=q1-(1.5*iqr)
ub=q3+(1.5*iqr)

outliers=d[(d<lb)|(d>ub)]
print(outliers)

print(lb)
print(ub)