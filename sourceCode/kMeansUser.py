##################################################################
# Date    : 2017-11-26											
# Author  : Krittaphat Pugdeethosapol (krittaphat.pug@gmail.com)
# Version : 1.0													
##################################################################
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
import csv

inputFile = open('../data/movieLens/MovieDocInfo.dat')
outputFile = open('../data/movieLens/MovieKMeansUser.dat', 'w')

iterLines = iter(inputFile)
dataID = []
data = []

for lineNum, line in enumerate(iterLines):
	dataID.append(line.split('::')[0])
	users = line.split('::')[1:]
	tmp = [0] * 672
	for us in users:
		tmp[int(us.split(',')[0])] = int(1)
	data.append(tmp)
	if lineNum > 1000:
		break
data = np.array(data, dtype='int')

numberLoop = np.array([500, 600, 700, 800, 900, 1000])
# kmeans = KMeans(n_clusters=100, random_state=0).fit(data)
# KMeans Clustering
# for n_clusters in range(500,1002):
for n_clusters in numberLoop:
	kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
	silhouette_avg = silhouette_score(data, kmeans.labels_)
	print('For n_clusters = {0} The average silhouette_score is : {1}'.format(n_clusters, silhouette_avg))

# for i in range(len(dataID)):
# 	outputFile.write('{0}::{1}\n'.format(dataID[i],kmeans.labels_[i]))
	# print('{0}::{1}'.format(dataID[i],kmeans.labels_[i]))

inputFile.close()
outputFile.close()





