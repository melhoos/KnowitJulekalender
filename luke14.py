
def ifUpSideDownNumber(number):
	upSideDownNumbers = ["0", "1", "6", "8", "9"]
	countUpSideDown = 0
	for n in str(number):
		if (n in upSideDownNumbers):
			countUpSideDown += 1
	if (len(str(number)) == countUpSideDown):
		return True
	else: 
		return False 

def palindromNumber(number):
	wrongwaynumber = str(number)[::-1]
	wwn = ""
	for n in wrongwaynumber:
		if (n == "6"):
			wwn += "9"
		elif (n == "9"):
			wwn+= "6"
		else:
			wwn += n
	if (str(number) == wwn):
		return True
	else:
		return False 

def run():
	count = 0
	for i in range(0,100000):
		if (ifUpSideDownNumber(i)):
			if (palindromNumber(i)):
				count += 1
	print count
	
run()
