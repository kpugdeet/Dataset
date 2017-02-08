##################################################################
# Date    : 2016-11-27											
# Author  : Krittaphat Pugdeethosapol (krittaphat.pug@gmail.com)
# Version : 1.0													
##################################################################
import pickle

inputFile = open('../data/movieLens/ratingsSortMovie.csv')
outputFile = open('../data/movieLens/DocInfoTmp.dat', 'w')
mapping = pickle.load(open('../data/movieLens/userKMap.object', 'rb' ))

prev = 0
iterLines = iter(inputFile)
for lineNum, line in enumerate(iterLines):
	if lineNum != 0:
		line = line.split(',')
		if (prev != int(line[1])):
			outputFile.write('\n')
			try:
				outputFile.write(mapping[line[1]])
			except:
				outputFile.write(line[1])
			prev = int(line[1])
		outputFile.write('::{0},{1}'.format(line[0],line[2]))

inputFile.close()
outputFile.close()





