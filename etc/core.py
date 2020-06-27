#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created By pikpikcu

import argparse,sys,time

def start():
	from etc.banner import Argument
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument("-c","--cms" , dest='cms')
	parser.add_argument("-H","--Host" , dest='host')
	parser.add_argument("-w","--wp" , dest='wp')
	parser.add_argument("-t","--thread" , dest='thread')
	parser.add_argument("-d","--dns" , dest='dns')
	parser.add_argument("-s","--subdo" , dest='subdo')
	parser.add_argument("-h","--help",dest='help',action='store_true')
	args = parser.parse_args()
	if args.help:
		Argument()
		exit()
	if args.subdo:
		from module.subdo import subdo
		time.sleep(2)
		subdo(args.subdo)
	if args.cms:
		from module.cms import cms
		time.sleep(2)
		cms(args.cms)
	if args.host:
		from module.host import host
		time.sleep(2)
		host(args.host)
	if args.wp:
		from module.wordpres import wp
		time.sleep(2)
		wp(args.wp)
	if args.thread:
		from module.finding import thread
		time.sleep(2)
		thread(args.thread)
	if args.dns:
		from module.dnsdumpster import dns
		time.sleep(2)
		dns(args.dns)
	 
