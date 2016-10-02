#! /usr/bin/python3
# Splitting Algorithm for Server Side interaction

import os
import sys

def printOptions():
	print ('OPTIONS')
	print ('-help to print this menu')
	print ('Argument format: [inputfilename] [numoutputfiles] [-o] [outputfilename]')

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

if(len(sys.argv) <= 2):
	printOptions()
	sys.exit(0)

elif((len(sys.argv) == 3) or (len(sys.argv) == 5)):
	inName,num = sys.argv[1:3]

	fid = 1
	size = os.path.getsize(inName)
	num = int(num)
	size = int(size / num)

	infile = open(inName, 'rb')
	if (len(sys.argv) == 3):
		strfile = inName + '_%d'
	else:
		outname = sys.argv[4]
		strfile = outname + '_%d'
	print ('Splitting file into {} parts'.format(num))
	while (fid <= num):
		print (fid)
		infile.seek((fid-1) * size)
		out = open(strfile %fid, 'wb+')
		out.write(infile.read(size))
		fid += 1;
	out.write(infile.read(size))
	print ('Completed splitting files')
		
else:
	operationMismatch(2)
