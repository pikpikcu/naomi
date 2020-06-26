#!/usr/bin/python

import os
import json
import requests
from pprint import pprint 
from etc.colors import *

api = open("Api.txt", "r+")
str = api.read()
def host(target):
	print(bcolors.red+"["+bcolors.green+"!"+bcolors.red+"]"+bcolors.green+" Detect the hosting URls: "+bcolors.red+target+bcolors.lightcyan+"\n")
	try:
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
		url = "https://www.who-hosts-this.com/API/Host?key="
		results = requests.get(url+str+"&url="+target,
								headers=headers).text
		data = json.loads(results)	
		#dump = json.dumps(data,sort_keys=True,indent=2) 
		pprint(data)
	except:
		pass