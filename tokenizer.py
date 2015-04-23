import nltk
import operator
import re
tokens=[]
def findToken(tok,nFiles):
    count=0
    for ii in range (0,nFiles):
        fo = open("./data/"+str(ii), "r")
        lines = fo.read()
       # print lines
        m = re.findall(tok, lines)
       # print m
        count+=len(m)
    return count
def tokenLen():
    return len(tokens)
def tokenize(fName):
    global tokens
    f=open(fName)
    text=f.read()
    tok=nltk.word_tokenize(text)
    for tk in tok:
        tokens.append(tk)
#    context(tokens)
def context(models):
    global tokens
#    print models
    cont=dict()
    totalMatches=0
    i=0
    for tok in tokens:
        #print tok
        if(tok in models):
            totalMatches+=1
            #tTup & tList is a temporary tuple that
            #will be used to map only the context to its count
            tlist=[]
            tTup=()
            #tmatchTup & tmatchlist is a temporary tuple that
            #will be used to map
            # the whole match to its count
            j=-2
            while(j<3):
                # j==0 means the word we matched
                if(j!=0):
                    tlist.append(tokens[i+j])
                j+=1
                tTup=tuple(tlist)
            if(cont.has_key(tTup)):
                cont[tTup]+=1
            else:
                cont[tTup]=1
        i+=1
    ret=list()
    #print cont
    #print totalMatches
    ret.append(cont)
    ret.append(totalMatches)
    return ret
def topModelPatterns(models,nFiles, nPatterns):
    global tokens
    if(len(models)==0):
        models=["Civic" ,"Camry" ,"Impreza" ,"Silverado","Tahoe", "GTI", "Corolla" ]
    print models
    cont=dict()
    totalMatches=0
    total=0
    ii=0
    if(len(tokens)==0):
        while(ii<=nFiles):
            tokenize("./data/"+str(ii))
            ii+=1
    ret=context(models)
    totalMatches=ret[1]
    cont=ret[0]
    #print cont
    PatternPmi(cont,totalMatches,len(tokens),nFiles)
    sorted_cont=list()
    for ii in range(nPatterns):
        max=0
        topKey=list()
        for keys in cont.keys():
            if(cont[keys]>max):
                max=cont[keys]
                topKey=keys
        del cont[topKey]
        sorted_cont.append(topKey)
   # print "###"
    #print sorted_cont
    #yprint "###"
    return sorted_cont

def PatternPmi(pattern,totalMatches,size,nFiles):
    #print totalMatches
    for key in pattern.keys():
        tp=totalPattern(key,nFiles)
        if(tp== 0 or totalMatches==0):
            pattern[key]=0
        else:
            pattern[key]=(pattern[key]*size)/(tp * totalMatches)
def MatchPmi(models_pattern,N,matches,model_total):
    if(matches==0 or model_total==0):
        return 0
    else:
        return((models_pattern*N)/(matches*model_total))
def totalPattern(key,nFiles):
    count=0
    for ii in range (0,nFiles):
        fo = open("./data/"+str(ii), "r")
        lines = fo.read()
        # print lines
               
	#print key
        m = re.findall(re.escape(key[0])+ "\s*" + re.escape(key[1]) + "\s*\w+\s*" + re.escape(key[2]) + "\s*"+ re.escape(key[3]), lines)
       # print m
        count+=len(m)
    return count
def yearTag(patternDict):
    for key in patternDict.keys():
        ii=0
        for word in key:
            try:
                int(word)
                if(int(word)>1900 and int(word) <2016):
                    #print "year is "+word
                    tList=[]
                    tupl=()
                    jj=0
                    for word2 in key :
                        #print str(jj)+","+str(ii)
                        if(jj==ii):
                            tList.append("YEAR")
                        else:
                            tList.append(word2)
                        jj+=1
                    tupl=tuple(tList)
                    value=patternDict[key]
                    del patternDict[key]
                    patternDict[tupl]=value
                    break
            except:
                pass
            ii+=1
    #print patternDict
    return patternDict
def main():
    print topModelPatterns(list())
if __name__ == "__main__":
    main()
