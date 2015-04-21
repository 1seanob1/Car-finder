import json
import urllib2
from os import listdir
from os.path import isfile, join
glob=0
def getFiles(dirName):
        try:
                itr=0
                #http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
                files=listdir(dirName)
                files2=[]
                for f in files:
                        if(isfile(join(dirName,f))):
                                itr=jRead(dirName,f,itr)
        except:
                pass
def write(text,itr):
        try:
                f=open("./data/"+str(itr),"w")
                f.write(text)
                f.close()
        except:
                pass
        #world
def get(html,itr):
        try:
                #http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
                write(urllib2.urlopen("http://"+html).read(),itr)
        except:
                pass
def jRead(dirName,fname,itr):
        try:
                #http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
                print dirName
                with open(join(dirName+"/",fname)) as json_data:
                        data=json.load(json_data)
                        for x in data:
                                get(fname+x["link"][0],itr)
                                itr+=1
                return itr
        except:
                pass
def main():
        glob=0
        getFiles("./data")
        #jRead("washingtondc.craigslist.org")
if __name__ == "__main__":
    main()
