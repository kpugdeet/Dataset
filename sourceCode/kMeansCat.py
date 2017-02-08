##################################################################
# Date    : 2017-11-26											
# Author  : Krittaphat Pugdeethosapol (krittaphat.pug@gmail.com)
# Version : 1.0													
##################################################################
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = open(dir_path+'/../data/movieLens/kMeansMovieData.csv')
outputFile = open(dir_path+'/../data/movieLens/MovieKMeans.dat', 'w')

# Key value
mapCat = {'key': -1, 'Adventure':0, 'Animation':1, 'Children':2, 'Comedy':3, 'Fantasy':4, 'Romance':5, 'Drama':6, 'Action':7, 'Crime':8, 'Thriller':9, 'Mystery':10, 'Horror':11, 'Sci-Fi':12, 'Documentary':13, 'IMAX':14, 'War':15, 'Musical':16, 'Western':17, 'Film-Noir':18, '(no genres listed)':19}

iterLines = iter(inputFile)
dataID = []
data = []
for lines in csv.reader(inputFile, skipinitialspace=True):
	dataID.append(lines[0])
	line = lines[2]
	category = line.split('|')
	tmp = [0] * 20
	for cat in category:
		tmp[mapCat[cat]] = int(1)
	data.append(tmp)
data = np.array(data, dtype='int')

kmeans = KMeans(n_clusters=20, random_state=0).fit(data)
# KMeans Clustering
# for n_clusters in range(1000,1001):
# 	kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
# 	silhouette_avg = silhouette_score(data, kmeans.labels_)
	# print('For n_clusters = {0} The average silhouette_score is : {1}'.format(n_clusters, silhouette_avg))

for i in range(len(dataID)):
	outputFile.write('{0}::{1}\n'.format(dataID[i],kmeans.labels_[i]))
	# print('{0}::{1}'.format(dataID[i],kmeans.labels_[i]))

print ('Done')
inputFile.close()
outputFile.close()





