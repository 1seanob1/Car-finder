import nltk
import tokenizer
import re

folder = 'data/'
goldStandard=dict()
modelCount_wMatch = dict()
modelCount = dict()
gold = list()

def countPattern(models):
        #totalMatch is the total number of times any pattern is found in the data
        totalMatch=0
        #totalModel is the total number of times a particular model/key is found in the text, regardless of patterns
        totalModel=0
	global goldStandard, gold, modelCount,modelCount_wMatch

	del goldStandard
        del modelCount_wMatch 
        del modelCount
        del gold 
        goldStandard=dict()
        modelCount_wMatch = dict()
        modelCount = dict()
        gold = list()
        
	print "Tokenize"
	goldStandard = tokenizer.topModelPatterns(models,99,7)
	gold = list(goldStandard) 
	
	print "Got Gold"  
#	print gold   
	for ii in range (0,99):
		
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
                                        print temp
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
        for model in modelCount_wMatch: 
                modelCount_wMatch[model]=tokenizer.MatchPmi(modelCount_wMatch[model],tokenizer.tokenLen(),totalMatch,tokenizer.findToken(model,99))
        models=list()
        for key in modelCount_wMatch.keys():
                if(modelCount_wMatch[key]>1000):
                        models.append(key)
        return models
        print modelCount_wMatch
		

models=list()
for ii in range(5):
        models=countPattern(models)
print models
print modelCount
print modelCount_wMatch

#print tokenizer.cont
#print gold[0]

