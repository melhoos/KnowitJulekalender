import datetime 
from dateutil.rrule import rrule, DAILY
def findFriday13ths():
	count = 0
	start = datetime.date(1337,1,1)
	end = datetime.date(2014,12,12)
	for day in rrule(DAILY, dtstart=start, until=end):
		dato = str(day).split(" ")
		dag = dato[0].split("-")
		if(4 == day.weekday() and dag[2] == str(13)):
			count += 1
	print count
findFriday13ths()