"""
Definer REGNESTYKKER til å være alle regnestykker hvor et tresifret tall blir summert med et annet tresifret tall, og resultatet er et firesifret tall. Alle tallene er positive heltall. Alle de 10 sifrene som utgjør et regnestykke skal inneholde hvert av sifrene 0-9 kun én gang.

Eksempler på slike regnestykker som oppfyller disse egenskapene er 324 + 765 = 1089 og 759 + 843 = 1602.

Hva er den minste verdien for et av leddene i REGNESTYKKER?

For eksemplene over (med kun de to regnestykkene) ville svaret vært 324, da det er det minste leddet.  

"""

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
