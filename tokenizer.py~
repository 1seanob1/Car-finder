import nltk
import operator
cont=dict()
total=0
def tokenize(fName):
    f=open(fName)
    text=f.read()
    tokens=nltk.word_tokenize(text)
    context(tokens)
def context(tokens):
    global total
    global cont
    models=["Mustang","Camry","Impreza","Silverado"]
    i=0
    for tok in tokens:
        if(tok in models):
            tlist=[]
            tTup=()
            j=-2
            while(j<3):
                if(j!=0):
                    tlist.append(tokens[i+j])
                j+=1
                tTup=tuple(tlist)
            if(cont.has_key(tTup)):
                cont[tTup]+=1
            else:
                cont[tTup]=1
            total+=1
        i+=1
def topPatterns():
    global cont
    global total
    #http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    sorted_cont=sorted(cont.items(), key=operator.itemgetter(1))
    return sorted_cont[len(sorted_cont)-1]
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
