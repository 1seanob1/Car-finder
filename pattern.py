import nltk
import tokenizer
import re

folder = 'data/'
goldStandard=dict()
modelCount_wMatch = dict()
modelCount = dict()
gold = list()
def countPattern():
        #totalMatch is the total number of times any pattern is found in the data
        totalMatch=0
        #totalModel is the total number of times a particular model/key is found in the text, regardless of patterns
        totalModel=0
	global goldStandard, gold, modelCount
	#loop
	print "Tokenize"
#	for ii in range (0,376):
		#tokenize
#		tokenizer.tokenize(folder+str(ii))		
		#toppatterns
	goldStandard = tokenizer.topModelPatterns(list())
	gold = list(goldStandard) 
	
	print "Got Gold"  
	print gold   
	for ii in range (0,99):
		
		fo = open(folder+str(ii), "r")
		lines = fo.read()
		#find_match
		m = re.findall(gold[0][0]+ ' ' + gold[0][1] + ' \w+ '+ gold[0][2] + ' '+ gold[0][3], lines)

                #Increment totalMatch by the number of times a pattern was found 
		totalMatch+=len(m)
		
		#extract models
		for element in m:
                        
                        totalMatch+=1
			temp = element.split()
			model = temp[2]
			#count		
			if modelCount_wMatch.has_key(model):
				modelCount_wMatch[model]+= 1
			else:
				modelCount_wMatch[model]= 1
		#nextfile
        for model in modelCount_wMatch: 
                #print model
                found = re.findall(model, lines)
                modelCount_wMatch[model]=tokenizer.MatchPmi(modelCount_wMatch[model],tokenizer.tokenLen(),totalMatch,len(found))
        
        print modelCount_wMatch
		



countPattern()
print modelCount
print modelCount_wMatch

#print tokenizer.cont
#print gold[0]

