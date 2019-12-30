import schedule
import time
import datetime

def function():
#	print("Alarm!!");
	file = open("./demofile.txt", "a")
	f.write(datetime.now().strtime("%H:%M:%S))
	f.close

schedule.every().day.at("14:00").do(function)

while 1:
    schedule.run_pending()
    time.sleep(1)
