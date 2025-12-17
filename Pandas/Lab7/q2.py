import pandas as pd

df = pd.DataFrame({
    'marks': [10, 12, 14, 15, 18, 20, 95]
})

Q1 = df['marks'].quantile(0.25)
Q3 = df['marks'].quantile(0.75)

IQR = Q3 - Q1


outliers = df[(df['marks'] < (Q1 - 1.5 * IQR)) | 
              (df['marks'] > (Q3 + 1.5 * IQR))]

print(outliers)


df_no_outliers = df[(df['marks'] >= (Q1 - 1.5 * IQR)) & 
                    (df['marks'] <= (Q3 + 1.5 * IQR))]

print(df_no_outliers)
from scipy import stats

df['z_score'] = stats.zscore(df['marks'])

outliers = df[df['z_score'].abs() > 3]
print(outliers)
df_no_outliers = df[df['z_score'].abs() <= 3]
print(df_no_outliers)
