#! /usr/bin/python3
# Compression/Decompression file for pressing files prior to encryption

import os
import sys
import zipfile

try:
	import zlib
	comp = zipfile.ZIP_DEFLATED
except:
	comp = zipfile.ZIP_STORED

def printOptions():
	print ('OPTIONS')
	print ('-help to print this menu')
	print ('Argument format: [-option] [inputfilename] [-o] [outputfilename]')
	print ('-c : Compress a file with ZIP archiving')
	print ('-d : Decompress a file with ZIP archiving')

def operationMismatch(num):
	if (num == 0):
		print ("ERROR: File was not found\n")
		sys.exit(0)	
	elif (num == 1):
		print ("ERROR: File could not be (de)compressed\n")
		sys.exit(0)
	elif (num == 2):
		print ("ERROR: Bad ZIP file\n")
		sys.exit(0)
	elif (num == 3):
		print ("ERROR: Invalid number of arguments (2 or 4 expected)\n")
		sys.exit(0)
	elif (num == 4):
		print ("ERROR: Invalid options")
		sys.exit(0)
if(len(sys.argv) == 2):
	printOptions()
	sys.exit(0)
elif(len(sys.argv) == 3):
	option,infile = sys.argv[1:3]
	
	output = "-o"
	if(option == "-c"):
		outfile = infile + ".zip"

elif(len(sys.argv) == 5):
	option,infile,output,outfile = sys.argv[1:5]
	if(option == "-c"):
		outfile += ".zip"

else:
	operationMismatch(3)

if(option == "-c"):
	print ('Compressing and Packing Archive')
	zip = zipfile.ZipFile(outfile, mode='w')
	try:
		print ('Adding ' + infile)
		zip.write(infile, compress_type = comp)
		print ('Done')
	except Exception:
		operationMismatch(1)
	finally:
		print ('Closing')
		zip.close()
	print
elif(option == "-d"):
	print ('Decompressing and Unpacking Archive')
	zip = zipfile.ZipFile(infile)
	try:
		print ('Extracting ' + infile)
		zip.extractall()
		print ('Done')
	except Exception:
		operationMismatch(1)
	finally:
		print ('Closing')
		zip.close()
else:
	operationMismatch(4)




























