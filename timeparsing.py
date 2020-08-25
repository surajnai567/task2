import datetime


def measure_time_difference(time2, time1, duration=15, format="%H:%M"):
	time1 = datetime.datetime.strptime(time1, format)
	time2 = datetime.datetime.strptime(time2, format)
	dura =  datetime.timedelta(days=0, minutes=duration)
	if time1-time2 >= dura:
		return True

	else:
		return False
