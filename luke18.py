import operator

def readFileAndFindAnagram(): 
	ordDict = {}  
	f = open("word.txt", "r")
	for word in f:
		wordSorted = "".join(sorted(word))
		if wordSorted in ordDict:
			ordDict[wordSorted] += 1 
		else: 
			ordDict[wordSorted] = 1 
	print sorted(ordDict.items(), key=operator.itemgetter(1))

readFileAndFindAnagram()