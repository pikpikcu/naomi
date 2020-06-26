#!/usr/bin/python

from etc.colors import *

def banner():
	print(bcolors.lightred+'''
>==>    >=>                        >=>       >=>     
>> >=>  >=>                        >> >=>   >>=>  >> 
>=> >=> >=>    >=> >=>     >=>     >=> >=> > >=>     
>=>  >=>>=>  >=>   >=>   >=>  >=>  >=>  >=>  >=> >=> 
>=>   > >=> >=>    >=>  >=>    >=> >=>   >>  >=> >=> 
>=>    >>=>  >=>   >=>   >=>  >=>  >=>       >=> >=> 
>=>     >=>   >==>>>==>    >=>     >=>       >=> >=>  
                        Created By:pikpikcu
                        Version:01[Beta]
	''')
def Argument():
	print(bcolors.lightgreen+"""
Options:
    -h,--help      | Show help message and exit
    -c,--cms	   | Detect the CMS and other technologies powering any website
    -H,--Host      | Detect the hosting providers for any website
    -w,--wp        | Detect which theme WordPress sites are using
    -t,--thread    | Use Threatcrowd for Finding domains
    -d,--dns       | Dnsdumster Mapping the domain
    -s,--subdo     | Use crt.sh for Enumerate Subdoamin

Example:
       python3 naomi.py <Options> example.com
""")