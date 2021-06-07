import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

df = pd.read_csv('stars_with_gravity.csv')
fig = px.scatter(df , x = 'Radius' , y = 'Mass')
fig.show()

x = df.iloc[:,[3,4]].values

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters=i,init = 'k-means++', random_state=54)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11),wcss,marker = 'o',color = 'red')
plt.title('the elbow method')
plt.xlabel('number_of_clusters')
plt.ylabel('wcss')
plt.show()

kmeans = KMeans(n_clusters=3,init = 'k-means++',random_state=42)
y_kmeans = kmeans.fit_predict(x)

plt.figure(figsize = (15,7))
sns.scatterplot(x[y_kmeans==0,0],x[y_kmeans==0,1],color = 'yellow',label = 'cluster1')
sns.scatterplot(x[y_kmeans==1,0],x[y_kmeans==1,1],color = 'blue' , label='cluster2')
sns.scatterplot(x[y_kmeans==2,0],x[y_kmeans==2,1],color = 'red' , label = 'cluster3')
sns.scatterplot(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1] , color = 'pink' , label = 'centroids', s = 100,marker = ',')
plt.title('clusters of stars')
plt.xlabel('Radius')
plt.ylabel('Mass')
plt.show()