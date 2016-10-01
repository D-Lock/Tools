#! /usr/bin/python3
# Encryption/Decryption file for crypting files prior to upload
# This uses AES Encryption to crypt the files into binaries
# MUST use a password atleast 16 characters long so the file is correctly
# padded

import os
import sys
#Create a command line arguement option
# OPTIONS:
def printOptions():
	print ("OPTIONS\n")
	print ("-help to print this menu")
	print ("Argument format: [-option] [inputfilename] [outputfilename] [password]\n")
	print ("-e : Encrypt a file with AES encryption\n")
	print ("-d : Decrypt a file with AES encryption\n")
	
def operationMismatch(num):
	if (num == 0):
		print ("ERROR: File was not found\n")
	elif (num == 1):
		print ("ERROR: File could not be encrypted\n")

#Get args
if (len(sys.argv)!=5):
	sys.exit("ERROR: Need 4 arguments in the correct format.")
script,option,in_filename,out_filename,password = sys.argv



#Encryption and Decryption fucntions
# modified code from StackOverFlow AES boilerplate encryption code
#/questions/16761458/

from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random

def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = ''
    while len(d) < key_length + iv_length:
        d_i = md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length+iv_length]

def encrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size
    salt = Random.new().read(bs - len('Salted__'))
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    out_file.write('Salted__' + salt)
    finished = False
    while not finished:
        chunk = in_file.read(1024 * bs)
        if len(chunk) == 0 or len(chunk) % bs != 0:
            padding_length = (bs - len(chunk) % bs) or bs
            chunk += padding_length * chr(padding_length)
            finished = True
        out_file.write(cipher.encrypt(chunk))

def decrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size
    salt = in_file.read(bs)[len('Salted__'):]
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''
    finished = False
    while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
        if len(next_chunk) == 0:
            padding_length = ord(chunk[-1])
            chunk = chunk[:-padding_length]
            finished = True
        out_file.write(chunk)

if (option == '-e'):
	with open(in_filename, 'rb') as in_file, open(out_filename, 'wb') as out_file:
    		encrypt(in_file, out_file, password)
	sys.exit(0)

elif (option =='-d'):
	with open(in_filename, 'rb') as in_file, open(out_filename, 'wb') as out_file:
    		decrypt(in_file, out_file, password)
	sys.exit(0)
else:
	exit("ERROR: Need to insert correct options, -e|-d")

