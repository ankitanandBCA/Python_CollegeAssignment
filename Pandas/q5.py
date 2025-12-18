import pandas as pd

d = pd.Series([-2, 10, 12, 14, 16, 18, 20, 200])

mean = d.mean()
std = d.std()


z_scores = (d - mean) / std

outliers = d[abs(z_scores) > 3]

print("Z-scores:")
print(z_scores)

print("\nOutliers:")
print(outliers)
