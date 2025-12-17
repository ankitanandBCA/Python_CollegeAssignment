import pandas as pd

df = pd.DataFrame({
    'math': [70, 80, 90, 60, 85],
    'science': [75, 82, 88, 65, 80],
    'english': [68, 78, 85, 58, 82]
})



corr = df['math'].corr(df['science'])
print(corr)


corr_matrix = df.corr()
print(corr_matrix)


df.corr(method='pearson')   # default
df.corr(method='spearman')
df.corr(method='kendall')
