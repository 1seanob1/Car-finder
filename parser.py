from os import listdir
from os.path import isfile, join
def getFiles(dirName):
#http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
	files=listdir(dirName)
	files2=[]
	for f in files:
		if(isfile(join(dirName,f))):
			files2.append(join(dirName,f))
	return files2
def parse(fileName):
	file=open(fileName,"r")
	lines=file.readlines()
	return lines

