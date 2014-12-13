

def isPrime(number):
	if (number == 2):
		return True
	elif (number == 1):
		return False
	for n in range(2, number): 
		if (number%n == 0 and n != number):
			return False
	return True

def isMirtall(number):
	rightway = number
	wrongway = int((str(number))[::-1])
	if( rightway != wrongway ):
		if (isPrime(rightway) and isPrime(wrongway)):
			return [rightway, wrongway]

def run():
	mirtallList = []
	tallList =  range(1,1000)
	for n in tallList:
		if (isMirtall(n) != None ): 
			[r,w] = isMirtall(n)
			if (r not in mirtallList and w not in mirtallList):
				mirtallList.append(r)
				mirtallList.append(w)
	print len(mirtallList)

run()

