#!/usr/bin/env python
#
# Created by:			Willi Ballenthin <william.ballenthin@mandiant.com> 2013
# Licence: 				Licensed under the Apache License, Version 2.0  
#						This means it is freely available for use and modification 
#						in a personal and professional capacity.
#
# Modified by:			Billy O Sullivan 2017
#
# Purpose:				This script parses windows event logs from windows 7 and up
# 						with the extension .evtx
#						It outputs the file to a terminal and also to a text file
#						called 'win_eventlog.txt'
#
# Usage:				python eventviewer.py <log file>
#
# Requirements:			python-evtx, available at https://github.com/williballenthin/python-evtx
#						install with pip - sudo pip install python-evtx


# Import libraries
import Evtx.Evtx as evtx
import Evtx.Views as e_views
import sys
from time import ctime


# Script usage
def usage():
	print '''
		--------------------
		-  eventviewer.py  -
		--------------------
	
Usage: python eventviewer.py <log file>
	
This script parses windows event logs from windows 7 and up
with the extension .evtx. It outputs the file to a terminal 
and also to a text file called 'win_eventlog.xml’ when run 
with admin privileges'''
	exit()

def main():
	
	if len(sys.argv) != 2:
		usage()
	elif sys.argv[1] == 'h': 				# If too many arguments or 'h' is used call usage
		usage()
	args = sys.argv[1]
	
	winlog = open('win_eventlog.xml', 'w')						# Prepair output file
	x = 'Script ran on: ' + ctime()
	winlog.write(x)
	x = '\n'
	winlog.write(x)
		
	try:
		with evtx.Evtx(args) as log:							# Convert file and output results
			print(e_views.XML_HEADER)
			winlog.write(e_views.XML_HEADER)
			print("<Events>")
			winlog.write("<Events>")
			for record in log.records():
				print(record.xml() + '\n')
				winlog.write(record.xml() + '\n')
			print("</Events>")
			winlog.write("</Events>")
	except:
		print 'Error!!!'
		usage()
	winlog.close()

if __name__ == "__main__":
	main()
