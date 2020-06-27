#!/usr/bin/python3

from threading import Thread
from etc.banner import banner

if __name__ == "__main__":
	from etc.core import start
	naomi = Thread(target=start)
	naomi.daemon = True
	naomi.start()
	try:
		banner()
		naomi.join()
	except:
		exit()
