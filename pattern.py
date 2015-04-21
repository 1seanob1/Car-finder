import nltk
import tokenizer
import re

folder = 'data2/'
goldStandard=dict()
modelCount = dict()
gold = list()
def countPattern():
	global goldStandard, gold, modelCount
	#loop
	print "Tokenize"
	for ii in range (0,376):
		#tokenize
		tokenizer.tokenize(folder+str(ii))		
		#toppatterns
	goldStandard = tokenizer.topPatterns()
	gold = list(goldStandard) 
	print "Got Gold"  
	print gold   
	for ii in range (0,376):
		
		fo = open(folder+str(ii), "r")
		lines = fo.read()
		#find_match
		m = re.findall(gold[0][0]+ ' ' + gold[0][1] + ' \w+ '+ gold[0][2] + ' '+ gold[0][3], lines)
		
		
		#extract models
		for element in m:
			temp = element.split()
			model = temp[2]
			#count		
			if modelCount.has_key(model):
				modelCount[model]+= 1
			else:
				modelCount[model]= 1
		
		#nextfile



countPattern()
print modelCount
#print tokenizer.cont
#print gold[0]

