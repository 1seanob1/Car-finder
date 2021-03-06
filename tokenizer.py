import nltk
import operator
import re
#import pattern
tokens=[]    
def findToken(match):
    count=0
    for tok in tokens: 
        if(tok==match):
            count+=1
    return count
def tokenLen():
    return len(tokens)
def tokenize(fName):
    global tokens
    f=open(fName)
    text=f.read()
    try:
        tok=nltk.word_tokenize(text)
        #tok=text.split()
        tok=tokenYearTag(tok)
        for tk in tok:
            tokens.append(tk)
        #    context(tokens)
    except:
        pass
def exportTokenize(fName):
    f=open(fName)
    text=f.read()
    tok=nltk.word_tokenize(text)
    #tok=text.split()
    tok=tokenYearTag(tok)
    return tok
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
            #HERE DEFINES SIZE OF PATTERN
            j=-1
            while(j<2):
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
#    print tokens
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
    cont=yearTag(cont)
    #print cont
    PatternPmi(cont,totalMatches,len(tokens),nFiles)

        #    print "sorted cont="+str( sorted_cont)
    return cont


def PatternPmi(pattern,totalMatches,size,nFiles):
    #print totalMatches
    for key in pattern.keys():
        tp=totalPattern(key,nFiles)
        if(tp== 0 or totalMatches==0):
            pattern[key]=0
        else:
            pattern[key]=(pattern[key]*size)/(tp * totalMatches)
def MatchPmi(models_pattern,N,matches,model_total):
    #print "matches= "+str(matches)+"\tmodel_total= "+str(model_total)
    if(matches==0 or model_total==0):
        return 0
    else:
        return((models_pattern*N)/(matches*model_total))
def totalPattern(key,nFiles):
    count=0
    ii=0
    for tok in tokens:
        if key[0]==tok:
            try:
                if(key[1]==tokens[ii+2]):
                    count+=1
            except Exception as err:
                #print err
                   #index out of bounds but I don't care
                pass
                   
        ii+=1
    # print m
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
def tokenYearTag(tokens):
    i=0
    for tok in tokens:
        try:
            if(int(tok)>1900 and int(tok) <2016):
                tokens[i]="YEAR"
        except:
            pass
        i+=1
    return tokens
def main():
    print topModelPatterns(list())
if __name__ == "__main__":
    main()
