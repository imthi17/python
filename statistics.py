import numpy as np
import pandas as pd


np.random.seed(0)
data = np.random.randn(100)


mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
q75, q25 = np.percentile(data, [75, 25])
iqr = q75 - q25


df = pd.DataFrame(data, columns=['Values'])
mean_pd = df['Values'].mean()
median_pd = df['Values'].median()
std_dev_pd = df['Values'].std()
iqr_pd = df['Values'].quantile(0.75) - df['Values'].quantile(0.25)


print("Using NumPy:")
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"IQR: {iqr:.2f}")

print("\nUsing Pandas:")
print(f"Mean: {mean_pd:.2f}")
print(f"Median: {median_pd:.2f}")
print(f"Standard Deviation: {std_dev_pd:.2f}")
print(f"IQR: {iqr_pd:.2f}")
