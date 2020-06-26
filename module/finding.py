#!/usr/bin/env python3

import os
import json
import requests
from pprint import pprint 
from etc.colors import *


def thread(target):
	print(bcolors.red+"["+bcolors.green+"!"+bcolors.red+"]"+bcolors.green+" Finding domains URls: "+bcolors.red+target+bcolors.lightcyan+"\n")
	try:
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
		
		url = "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain="
		results = requests.get(url+target,
								headers=headers).text
		data = json.loads(results)
		pprint(data)	
		#dump = json.dumps(data,sort_keys=True,indent=4) 
		#print(dump)
	except:
		pass




	
