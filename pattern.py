import nltk
import tokenizer
import re

folder = 'data/'
goldStandard=dict()

modelCount = dict()
gold = list()
models={"Civic" : 0 ,"Camry" : 0 ,"Impreza" : 0 ,"Silverado" : 0,"Tahoe" : 0, "GTI" : 0, "Corolla" : 0 }
def getTopPattern(patterns):
        print patterns
        print
        max=0
        topKey=list()
        maxm=0
        for keys in patterns.keys():
                if(patterns[keys]>maxm and (keys not in gold) ):
                        maxm=patterns[keys]
                        topKey=keys
                
        gold.append(topKey)
def countPattern(nFiles):

        #totalMatch is the total number of times any pattern is found in the data
        totalMatch=0
        #totalModel is the total number of times a particular model/key is found in the text, regardless of patterns
        totalModel=0
	global goldStandard, gold, modelCount,models

        modelCount_wMatch = dict()
        #get list of keys from modelCount_wMatch to feed to topModelPatterns
        tempPattern = tokenizer.topModelPatterns(models.keys(),nFiles,1)
        getTopPattern(tempPattern)
        #add top pattern to goldStandard of patterns
        ii=0
        for tok in tokenizer.tokens:
                for strings in gold:
                        if(tok==strings[0]):
                                print "###"
                                print(tokenizer.tokens[ii]+" "+tokenizer.tokens[ii+1]+" "+tokenizer.tokens[ii+2])
                                print(strings[0]+" "+strings[1])
                                print "###"
                        try:
                                if(strings[0]==tok and strings[1]==tokenizer.tokens[ii+2]):
                                        if(modelCount_wMatch.has_key(tokenizer.tokens[ii+1])):
                                                modelCount_wMatch[modeltokenizer.tokens[ii+1]]+= 1
                                        else:
                                                modelCount_wMatch[modeltokenizer.tokens[ii+1]]= 1
                        except:
                                pass
                ii+=1
        #print modelCount_wMatch
        for model in modelCount_wMatch: 
                modelCount_wMatch[model]=tokenizer.MatchPmi(modelCount_wMatch[model],tokenizer.tokenLen(),totalMatch,tokenizer.findToken(model,nFiles))
        print modelCount_wMatch
        models = addMax(modelCount_wMatch,models)
        #print modelCount_wMatch
        #remove models below pmi threshold
        #print"modelcountwmatch="
        #print modelCount_wMatch
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
for ii in range(10):
        countPattern(99)
print models

#print tokenizer.cont
#print gold[0]

