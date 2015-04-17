import nltk
import tokenizer
import re

folder = 'data/'
goldStandard=dict()
gold = list()
def countPattern():
	global goldStandard, gold
	#loop
	for ii in range (0,99):
		#tokenize
		tokenizer.tokenize(folder+str(ii))		
		#toppatterns
	goldStandard = tokenizer.topPatterns()
	gold = list(goldStandard)      
	for ii in range (0,99):
		fo = open(folder+str(ii), "r")
		lines = fo.read()
		re.match(/gold[0][0]gold[0][1]\w+gold[0][2]gold[0][3]/g, lines)

		#find_match
		#count
		#nextfile



countPattern()
#print tokenizer.cont
#print gold[0]

