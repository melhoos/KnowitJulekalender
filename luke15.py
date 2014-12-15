def isMultiply(number1, number2):
	numberList = [str(number1)[0], str(number1)[1], str(number2)[0], str(number2)[1] ]
	multiply = number1 * number2
	if (len(str(multiply)) == 4):
		for n in str(multiply):
			if n in numberList:
				numberList.remove(n)
	if (len(numberList) == 0 ):
		return True
	else:
		return False 

def isDivisibleTen(num):
	if (num%10 == 0):
		return True
	else:
		return False

def run():
	possibleList = []
	for x in range(10,99):
		for y in range(10,99):
			if (isMultiply(x,y)):
				if ( (isDivisibleTen(x) != isDivisibleTen(y)) or ( isDivisibleTen(x) == False and isDivisibleTen(y) == False)):
					if ( (x*y) not in possibleList ):
						possibleList.append(x*y)
	print len(possibleList)


run() 
