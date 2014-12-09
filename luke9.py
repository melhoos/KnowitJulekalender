
import time
def countNumbers():
	everyCombination = [] 
	for n in range(100,1000):
		for m in range(500,1000):
			numSum = m + n
			if checkNum(n,m,numSum) == True:
				everyCombination.append(min(n,m))
	print min(everyCombination)

def checkNum(n,m,numSum):
	all_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	for number in str(n):
		if number in all_numbers:
			all_numbers.remove(number)
		else:
			return False 
	for number in str(m):
		if number in all_numbers:
			all_numbers.remove(number)
		else:
			return False
	for number in str(numSum):
		if number in all_numbers:
			all_numbers.remove(number)
		else: 
			return False 
	if len(all_numbers) == 0:
		return True
	else:
		return False

start_time = time.time()
countNumbers()
print "--- {0} seconds ---".format(time.time() - start_time)
