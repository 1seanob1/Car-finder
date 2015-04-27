import nltk
import tokenizer
import re

folder = 'data/'
goldStandard=dict()

modelCount = dict()
gold = list()
models={"Civic" : 0 ,"Camry" : 0 ,"Impreza" : 0 ,"Silverado" : 0,"Tahoe" : 0, "GTI" : 0, "Corolla" : 0 }
def getTopPattern(patterns):
        #print patterns
        #print
        max=0
        topKey=list()
        maxm=0
        for keys in patterns.keys():
                if(patterns[keys]>maxm and (keys not in gold) ):
                        maxm=patterns[keys]
                        topKey=keys
        gold.append(topKey)
def countPattern(nFiles,tokens):

        #totalMatch is the total number of times any pattern is found in the data
        totalMatch=0

	global goldStandard, gold, modelCount,models

        #temporary list for matches found in this iteration
        modelCount_wMatch = dict()
        #get list of keys from modelCount_wMatch to feed to topModelPatterns
        tempPattern = tokenizer.topModelPatterns(models.keys(),nFiles,1)

        #add top pattern to goldStandard of patterns
        getTopPattern(tempPattern)
       
        #find Matches
        ret=findMatches(tokens,modelCount_wMatch)
        totalMatch=ret["totalMatch"]
        modelCount_wMatch=ret["models"]

        #PMI conversion
        for model in modelCount_wMatch: 
                modelCount_wMatch[model]=tokenizer.MatchPmi(modelCount_wMatch[model],tokenizer.tokenLen(),   totalMatch    ,tokenizer.findToken(model))
                
        #add top new model to goldModels
        models = addMax(modelCount_wMatch,models)

def findMatches(tokens,modelCount_wMatch):
        global gold
        totalMatch=0
        ii=0
        for tok in tokens:
                for strings in gold:
                        try:
                                if(strings[0]==tok and strings[1]==tokens[ii+2]):
                                        totalMatch+=1
                                        print "The match= "+tokens[ii+1]+"\n"
                                        if(modelCount_wMatch.has_key(tokens[ii+1])):
                                                modelCount_wMatch[tokens[ii+1]]+= 1
                                        else:
                                                modelCount_wMatch[tokens[ii+1]]= 1
                        except Exception as inst:
                                #print inst
                                pass
                ii+=1
        #print modelCount_wMatch
        return {"models":modelCount_wMatch, "totalMatch" : totalMatch}
def addMax(Count_wMatch,topMatches):
        #adds the max value from seaching patterns to modles list
        maxm=0
        maxModel=""
        for key in Count_wMatch.keys():
                if(Count_wMatch[key]>maxm and (key not in topMatches)):
                        maxm=Count_wMatch[key]
                        maxModel=key
        #print maxModel+"="+str(maxm)
        topMatches[maxModel]=maxm
        
        return topMatches
def initOdometer():
        global models,gold
        del models
        models={"100K" : 0,"200K" :0, "100,000" : 0, "100000" : 0}
        del gold
        gold=list()
def initColor():
        global models,gold
        del models
        models={"Tan" : 0,"Red" :0, "Yellow" : 0, "Black" : 0}
        del gold
        gold=list()
def evaluate(fname):
        global gold

        tokens=tokenizer.exportTokenize(fname)
        modelCount_wMatch=dict()
        ret=findMatches(tokens,modelCount_wMatch)
        modelCount_wMatch=ret["models"]
        totalMatch=ret["totalMatch"]
        #PMI conversion
        for model in modelCount_wMatch: 
                modelCount_wMatch[model]=tokenizer.MatchPmi(modelCount_wMatch[model],len(tokens),   totalMatch    ,tokenizer.findToken(model))
        print addMax(modelCount_wMatch,dict())

ii=0
nFiles=300
while(ii<=nFiles):
        tokenizer.tokenize("./data/"+str(ii))
        ii+=1
for ii in range(25):
        countPattern(nFiles,tokenizer.tokens)        
print models
evaluate("./data/0")
initOdometer()
for ii in range(15):
        countPattern(nFiles,tokenizer.tokens)
print models
evaluate("./data/99")
initColor()
for ii in range(15):
        countPattern(nFiles,tokenizer.tokens)
print models
evaluate("./data/99")



#print tokenizer.cont
#print gold[0]

