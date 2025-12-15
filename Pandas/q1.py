import pandas as pd


df = pd.DataFrame({
    'col1': [2, 1, 2, 1],
    'col2': [4, 3, 2, 1]
})


df = df.sort_values(by=['col1', 'col2'], ascending=[True, False])

df = df.sort_index(ascending=False)

print(df)
