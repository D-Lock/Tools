#! /usr/bin/python3
# Encryption/Decryption file for crypting files prior to upload

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
script,option,inputfile,outputfile,password = sys.argv



#Encryption and Decryption fucntions
# modified code from StackOverFlow AES boilerplate encryption code
#/questions/16761458/

from os import urandom
from hashlib import md5

from Crypto.Cipher import AES

def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = b'' 
    while len(d) < key_length + iv_length:
        d_i = md5(d_i + str.encode(password) + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length+iv_length]
#encrypts a file based on the input and output file using password from input
def encrypt(in_file, out_file, password, salt_header='', key_length=32):
    bs = AES.block_size
    salt = urandom(bs - len(salt_header))
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    of = open(out_file,'wb')
    of.write(str.encode(salt_header) + salt)
    i_f = open(in_file,'rb')
    finished = False
    while not finished:
        chunk = i_f.read(1024 * bs) 
        if len(chunk) == 0 or len(chunk) % bs != 0:
            padding_length = (bs - len(chunk) % bs) or bs
            chunk += str.encode(
                padding_length * chr(padding_length))
            finished = True
        of.write(cipher.encrypt(chunk))
    of.close()
    i_f.close()
#Decrypts a file based on the input files and passwords which is hashed with derive_key_and_iv
def decrypt(in_file, out_file, password, salt_header='', key_length=32):
    bs = AES.block_size
    i_f = open(in_file,'rb')
    salt = i_f.read(bs)[len(salt_header):]
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''
    finished = False
    of = open(out_file,'wb')
    while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(
            i_f.read(1024 * bs))
        if len(next_chunk) == 0:
            padding_length = chunk[-1]  
            chunk = chunk[:-padding_length]
            finished = True 
            of.write(
                bytes(x for x in chunk))
    of.close()
    i_f.close()
if (option == '-e'):
	encrypt(inputfile,outputfile,password)
	sys.exit(0)

elif (option =='-d'):
	decrypt(inputfile,outputfile,password)
	sys.exit(0)
else:
	exit("ERROR: Need to insert correct options, -e|-d")

