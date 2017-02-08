##################################################################
# Date    : 2016-11-21											
# Author  : Krittaphat Pugdeethosapol (krittaphat.pug@gmail.com)
# Version : 1.0													
##################################################################
import tmdbsimple as tmdb
import time
import re
import os
import string
import pickle
import json, requests

url = 'http://www.omdbapi.com/'
inputFiles = open('../data/movieLens/movies.csv')
output = {'key':'value'}

PATTERN = re.compile(r'''((?:[^,"]|"[^"]*")+)''')

count = 0
inputLines = iter(inputFiles)
for lineNum, line in enumerate(inputLines):
	line = line.rstrip()
	if lineNum != 0:
		count += 1
		movieName = PATTERN.split(line)[1::2][1]
		movieName = re.split('\(|,|:', movieName)[0]
		print(PATTERN.split(line)[1::2][0] + ' ' + movieName)
		parameters = dict(plot='full',t=movieName)
		resp = requests.get(url=url, params=parameters)
		data = json.loads(resp.text)
		if data['Response'] == 'True':
			output[line.split(',')[0]] = data['imdbID'].encode('utf-8')
			output[data['imdbID'].encode('utf-8')] = line.split(',')[0]
		time.sleep(0.25)
print(count)
inputFiles.close()
pickle.dump(output, open('../data/movieLens/userKMap.object','wb'))

	





