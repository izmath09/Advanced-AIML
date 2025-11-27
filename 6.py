import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
data=pd.DataFrame(iris.data,columns=iris.feature_names)
x=pd.get_dummies(data)
k=3
kmeans=KMeans(n_clusters=k,random_state=42)

kmeans.fit(x)
l_kmeans=kmeans.labels_
gmm=GaussianMixture(n_components=k,random_state=42)
gmm.fit(x)
l_gmm=gmm.predict(x)
score_k=silhouette_score(x,l_kmeans)
score_g=silhouette_score(x,l_gmm)
print(f'Silhouette Score for KMeans: {score_k:.3f}')
print(f'Silhouette Score for EM: {score_g:.3f}')
if score_k>score_g:
print("KMeans performs better.")
else:
print("EM performs better.")
plt.bar(["Kmneans","Em"],[score_k,score_g],color=['blue','orange'])
plt.title('Silhouette Scores Comparison')
plt.ylabel('Silhouette Score')
plt.ylim(0,1)
plt.show()
