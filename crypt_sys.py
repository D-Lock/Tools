#! /usr/bin/python3
# Encryption/Decryption file for crypting files prior to upload

import os
import sys
#Create a command line arguement option
# OPTIONS:
def printOptions():
	print "OPTIONS\n"
	print "-help to print this menu"
	print "Argument format: [-option] [inputfilename] [outputfilename] [password]\n"
	print "-e : Encrypt a file with AES encryption\n"
	print "-d : Decrypt a file with AES encryption\n"
	
def operationMismatch(num):
	if (num == 0):
		print "ERROR: File was not found\n"
	elif (num == 1):
		print "ERROR: File could not be encrypted\n"

#Get args
if (len(sys.argv)!=4):
	sys.exit("ERROR: Need 4 arguments in the correct format.")
option,inputfile,outputfile,password = argv

if (option == '-e'):
	encrypt(inputfile,outputfile,password)
	sys.exit(0)

elif (option =='-d'):
	decrypt(inputfile,outputfile,password)
	sys.exit(0)
else:
	exit("ERROR: Need to insert correct options, -e|-d")

#Encryption and Decryption fucntions
