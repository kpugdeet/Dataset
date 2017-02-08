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

tmdb.API_KEY = '86f3a72a97a34847d86cfccdff810336'
search = tmdb.Search()

inputFiles = open('../data/movieLens/moviesDetail.csv')
outputFiles = open('../data/movieLens/moviesDetailTmp.csv','w')

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
			try:
				movieName = PATTERN.split(line)[1::2][1].split('(', 1)[0]
				print(PATTERN.split(line)[1::2][0] + ' ' + movieName)
				response = search.movie(query=movieName)
				if search.results[0]['overview'] != '':
					outputFiles.write('{0},{1}\n'.format(line,search.results[0]['overview'].encode('utf-8').replace(",", "").translate(string.maketrans("\n\t\r", "   "))))
				else:
					outputFiles.write('{0}\n'.format(line))
				time.sleep(0.25)
			except:
				outputFiles.write('{0}\n'.format(line))
				continue
		else:
			outputFiles.write('{0}\n'.format(line))
os.system('mv ../data/movieLens/moviesDetailTmp.csv ../data/movieLens/moviesDetail.csv')
print(count)

inputFiles.close()
outputFiles.close()
	





