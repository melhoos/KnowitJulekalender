def run():
	string = "472047"
	for n in range(0, 10000):
		if (string in str(2**n)):
			print n
			break
run()

