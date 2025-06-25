import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('sales_data.csv')

# Select relevant columns
df = df[['CUSTOMERNAME', 'SALES']]

# Scale numerical columns
scaler = StandardScaler()
df[['SALES']] = scaler.fit_transform(df[['SALES']])





from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Specify number of clusters
n_clusters = 3

# Apply K-Means clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['SALES']])

# Visualize clusters
sns.scatterplot(x='CUSTOMERNAME', y='SALES', hue='Cluster', palette='Set1', data=df)
plt.show()


DBSCAN Clustering


from sklearn.cluster import DBSCAN

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=10)
df['Cluster'] = dbscan.fit_predict(df[['SALES']])

# Visualize clusters
sns.scatterplot(x='CUSTOMERNAME', y='SALES', hue='Cluster', palette='Set1', data=df)
plt.show()

