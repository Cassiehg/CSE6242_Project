#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:08:40 2018

@author: chriskwan
"""
import numpy as np
from sklearn.cluster import KMeans
from copy import deepcopy
import pandas as pd
from matplotlib import pyplot as plt
 

# =============================================================================
# def fun(input_file, output_file:
#     with open(input_file, 'rb') as inp, open(output_file, 'w') as out:
#         
#         f = 
# =============================================================================
    
     

    
    
    
#if __name__ == '__main__':
#    fun()
plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')

#import data
data = pd.read_csv('20180329_removed_empty_long_lat_vals.csv')
print(data.shape)
#number of rows to view
data.head()
#print("rows: ", data.head())

#getting the values and plot it
f1 = data['Latitude'].values
f2 = data['Longitude'].values
X = np.array(list(zip(f1,f2)))
#plt.scatter(f1, f2, c='black', s=7)

#number of clusters
kmeans = KMeans(n_clusters=100, max_iter=300)
#fit input data
kmeans = kmeans.fit(X)
#get cluster labels
labels = kmeans.predict(X)
#centroid values
centroids = kmeans.cluster_centers_

#print(centroids.shape, centroids_x.shape, centroids_y.shape)
plt.scatter(X[:, 0], X[:, 1],c = kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 50, c = 'yellow')
#print(labels)
#print(kmeans.labels_)
#print(X[:,0])

#plt.scatter(centroid)


#save output file
d_lat_long = {'lat': X[:, 0],'long': X[:,1]}
df = pd.DataFrame(data=d_lat_long)

d_centers = {'lat_center': kmeans.cluster_centers_[:, 0],'long_center': kmeans.cluster_centers_[:, 1]}
df_centers = pd.DataFrame(data=d_centers)

df_centers.to_csv('100_centers_lat_long.csv', sep=',')




