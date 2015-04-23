import nltk
import tokenizer
import re

folder = 'data/'
goldStandard=dict()

modelCount = dict()
gold = list()
models={"Civic" : 0 ,"Camry" : 0 ,"Impreza" : 0 ,"Silverado" : 0,"Tahoe" : 0, "GTI" : 0, "Corolla" : 0 }
def getTopPattern(patterns):
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
	print "Tokenize"
        modelCount_wMatch = dict()
        #get list of keys from modelCount_wMatch to feed to topModelPatterns
        ###
        temp=list()
        for key in models:
                temp.append(key)
        ###

        ###
	tempPattern = tokenizer.topModelPatterns(temp,nFiles,1)
        getTopPattern(tempPattern)
        #add top pattern to goldStandard of patterns
        print "$$$"
        print gold
        print"$$$"
        # gold   
	for ii in range (0,nFiles):		
		fo = open(folder+str(ii), "r")
		lines = fo.read()
		#find_match
                m=list()
                for strg in gold:
                        m=re.findall(re.escape(strg[0])+ "\s*" + re.escape(strg[1]) + "\s*\w+\s*" + re.escape(strg[2]) + "\s*"+ re.escape(strg[3]), lines)
                        #Increment totalMatch by the number of times a pattern was found 
                        totalMatch+=len(m)
                        #extract models
                        if(len(m)>0):
                                for element in m:
                                        totalMatch+=1
                                        temp=element.split()
                                        try:
                                                model = temp[2]
                                                #count		
                                                if modelCount_wMatch.has_key(model):
                                                        modelCount_wMatch[model]+= 1
                                                else:
                                                        modelCount_wMatch[model]= 1
                                        except:
                                                pass
		#nextfile
        #print modelCount_wMatch
        for model in modelCount_wMatch: 
                modelCount_wMatch[model]=tokenizer.MatchPmi(modelCount_wMatch[model],tokenizer.tokenLen(),totalMatch,tokenizer.findToken(model,nFiles))

        #remove models below pmi threshold
        maxm=0
        maxModel=""
        #print"modelcountwmatch="
        #print modelCount_wMatch
        for key in modelCount_wMatch.keys():
                if(modelCount_wMatch[key]>maxm and (key not in models)):
                        maxm=modelCount_wMatch[key]
                        maxModel=key
        #print maxModel+"="+str(maxm)
        models[maxModel]=maxm

for ii in range(5):
        countPattern(99)
print models

#print tokenizer.cont
#print gold[0]

