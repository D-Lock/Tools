#! /usr/bin/python3
# Merging Algorithm for Server Side interaction

import os
import sys

def printOptions():
	print ('OPTIONS')
	print ('-help to print this menu')
	print ('Argument format: [firstPart] [numfiles] [-o] [outputfilename]')

def operationMismatch(num):
	if (num == 0):
		print ("ERROR: File was not found\n")
		sys.exit(0)	
	elif (num == 1):
		print ("ERROR: File could not be merged\n")
		sys.exit(0)
	elif (num == 2):
		print ("ERROR: Invalid arguments (3 or more expected)\n")
		sys.exit(0)

if(len(sys.argv) <= 2):
	printOptions()
	sys.exit(0)

elif((len(sys.argv) == 3) or (len(sys.argv) == 5)):
	inName,num = sys.argv[1:3]
	
	inPath = os.path.join(os.getcwd(), inName)
	size = os.path.getsize(inPath)
	last = inName.rfind("_")
	if(len(sys.argv) == 3):
		outName = inName[:last]
		strfile = outName + '_%d'
	else:
		outName = sys.argv[4]
		strfile = inName[:last] + '_%d'

	cwd = os.getcwd()
	out = open(os.path.join(cwd, outName), 'wb+')

	print ('Merging file from {} parts'.format(num))
	for i in range(1,int(num)+1):
		infile = open(os.path.join(cwd, strfile %i), 'rb')
		out.write(infile.read(size))
	print ('Completed merging files')

else:
	operationMismatch(2)
