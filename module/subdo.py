#!/usr/bin/python
import re,sys
from requests import get
from etc.colors import *


def subdo(domain):
    print(bcolors.red+"["+bcolors.green+"!"+bcolors.red+"]"+bcolors.green+" Enumerate Subdomains URls: "+bcolors.red+domain+bcolors.lightcyan+"\n")
    url = 'https://crt.sh/?q='
    req = get(url+domain).text
    regex_title = re.compile(r"(<TD></TD><TD><A)(?<=TD>).*?(?=<)")
    title = re.findall(regex_title,req)
    print(title)
    
