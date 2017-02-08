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
import json, requests

url = 'http://www.omdbapi.com/'
inputFiles = open('../data/movieLens/movies.csv')
outputFiles = open('../data/movieLens/moviesDetailOMDB.csv','w')

PATTERN = re.compile(r'''((?:[^,"]|"[^"]*")+)''')

count = 0
inputLines = iter(inputFiles)
for lineNum, line in enumerate(inputLines):
	line = line.rstrip()
	if lineNum == 0:
		outputFiles.write('{0}\n'.format(line))
	else:
		if len(PATTERN.split(line)[1::2]) < 4:
			count += 1
			movieName = PATTERN.split(line)[1::2][1]
			movieName = re.split('\(|,|:', movieName)[0]
			print(PATTERN.split(line)[1::2][0] + ' ' + movieName)
			parameters = dict(plot='full',t=movieName)
			resp = requests.get(url=url, params=parameters)
			data = json.loads(resp.text)
			if data['Response'] == 'True':
				outputFiles.write('{0},{1}\n'.format(line,data['Plot'].encode('utf-8').replace(",", "").translate(string.maketrans("\n\t\r", "   "))))
			else:
				outputFiles.write('{0}\n'.format(line))
			time.sleep(0.25)
		else:
			outputFiles.write('{0}\n'.format(line))
# os.system('mv ../data/movieLens/moviesDetailTmp.csv ../data/movieLens/moviesDetail.csv')
print(count)

inputFiles.close()
outputFiles.close()
	





