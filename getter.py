import json
import urllib2
from os import listdir
from os.path import isfile, join
glob=0
def getFiles(dirName):
        itr=0
#http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
	files=listdir(dirName)
	files2=[]
	for f in files:
		if(isfile(join(dirName,f))):
                        itr=jRead(f,itr)
def write(text,itr):
        f=open("./data/"+str(itr),"w")
        f.write(text)
        f.close()
        #world
def get(html,itr):
        #http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
        write(urllib2.urlopen("http://"+html).read(),itr)
def jRead(fname,itr):
#http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
        with open(fname) as json_data:
                data=json.load(json_data)
        for x in data:
                get(fname+x["link"][0],itr)
                itr+=1
        return itr
def main():
        glob=0
        getFiles("./data")
        #jRead("washingtondc.craigslist.org")
if __name__ == "__main__":
    main()
