#! /usr/bin/python3
# Compression/Decompression file for pressing files prior to encryption

import os
import sys

def printOptions():
	print ('OPTIONS')
	print ('-help to print this menu')
	print ('Argument format: [inputfilename] [numoutputfiles]')

def operationMismatch(num):
	if (num == 0):
		print ("ERROR: File was not found\n")
		sys.exit(0)	
	elif (num == 1):
		print ("ERROR: File could not be split\n")
		sys.exit(0)
	elif (num == 2):
		print ("ERROR: Invalid number of arguments (2 or 4 expected)\n")
		sys.exit(0)

if(len(sys.argv) == 2):
	printOptions()
	sys.exit(0)

elif(len(sys.argv) == 3):
	inName,num = sys.argv[1:3]
	(int) size = os.stat(inName)/num
	fid = 1

	infile = open(inName)
	strfile = inName + '_%d'
	while (fid <= num):
		f = open(strfile %fid, 'w')
		

else:
	operationMismatch(2)
