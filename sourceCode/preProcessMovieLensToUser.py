##################################################################
# Date    : 2016-11-27											
# Author  : Krittaphat Pugdeethosapol (krittaphat.pug@gmail.com)
# Version : 1.0													
##################################################################

inputFile = open('../data/movieLens/ratings.csv')
outputFile = open('../data/movieLens/UserInfo.dat', 'w')

prev = 0
iterLines = iter(inputFile)
for lineNum, line in enumerate(iterLines):
	if lineNum != 0:
		line = line.split(',')
		if (prev != int(line[0])):
			outputFile.write('\n')
			outputFile.write(line[0])
			prev = int(line[0])
		outputFile.write('::{0},{1}'.format(line[1],line[2]))

inputFile.close()
outputFile.close()





