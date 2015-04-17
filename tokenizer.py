import nltk
import operator
models=dict()
modelWithCont=dict()
cont=dict()
totalPatterns=0
totalMatches=0
total=0
def tokenize(fName):
    f=open(fName)
    text=f.read()
    tokens=nltk.word_tokenize(text)
    context(tokens)
def context(tokens):
    global totalPatterns, totalMatches,total
    global cont, modelWithCont, models
    models={"Mustang" : 0 ,"Camry" : 0 ,"Impreza" : 0 ,"Silverado" : 0}
    i=0
    for tok in tokens:
        total+=1
        if(tok in models):
            #increase the count of this token
            models[tok]+=1
            totalMatches+=1
            #tTup & tList is a temporary tuple that
            #will be used to map only the context to its count
            tlist=[]
            tTup=()
            #tmatchTup & tmatchlist is a temporary tuple that
            #will be used to map
            # the whole match to its count
            tMatchList=[]
            tMatchTup=()
            j=-2
            while(j<3):
                if(j!=0):
                    tlist.append(tokens[i+j])
                    tMatchList.append(tokens[i+j])
                else:
                    #add the match to the tMatchList
                    tMatchList.append(tokens[i])
                j+=1
                tTup=tuple(tlist)
                tMatchTup=tuple(tMatchList)
            if(cont.has_key(tTup)):
                cont[tTup]+=1
            else:
                cont[tTup]=1
            if(modelWithCont.has_key(tMatchTup)):
                modelWithCont[tMatchTup]+=1
            else:
                modelWithCont[tMatchTup]=1
            totalPatterns+=1
        i+=1
    return cont
def topPatterns():
    global cont, models,modelWithCont
    global totalMatches, totalPatterns,total
    PatternPmi(cont,totalMatches,total)
    #http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    sorted_cont=sorted(cont.items(), key=operator.itemgetter(1))
    return sorted_cont[len(sorted_cont)-1]
def PatternPmi(pattern,totalMatches,size):
    for key in pattern.keys():
        pattern[key]=(pattern[key]*size)/(pattern[key]*totalMatches)
               
def main():
    ii=0
    while(ii<100):
        tokenize("./data/"+str(ii))
        ii+=1
    if cont:
        print cont
    print "\n"
    print topPatterns()
if __name__ == "__main__":
    main()
