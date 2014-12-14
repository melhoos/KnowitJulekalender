def isPrime(number):
	if (number == 2):
		return True
	elif (number == 1):
		return False
	for n in range(2, number): 
		if (number%n == 0 and n != number):
			return False
	return True

def isMirptall(number):
	return number != int((str(number))[::-1]) and isPrime(number) and isPrime(int((str(number))[::-1]))

def run():
	mirps = 0 
	for n in range(1,1000):
		if isMirptall(n):
			mirps += 1
	print mirps

run()

