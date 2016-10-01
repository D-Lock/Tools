#! /usr/bin/python3
# Encryption/Decryption file for crypting files prior to upload

import os
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

