# Tools
Merging, Splitting and Encrypting Tools for D-Lock
## Encryption
crypt_sys uses AES encryption to block cipher the binary file that is chosen and outputs the result to a file
 Syntax:
  - [-e|-d] [inputfile] [outputfile] [password that is exactly 16 characters]
  -e: encrypts the input file with AES that is salted from the password and random number generation from the Python Crypto package
  -d: decrypts the input file with AES from the password given and returns the file to the output filename/pathname specificied.
  
  The password needs to be 16 characters, and preferred to have capitals, special characters under ASCII and  numbers for security purposes.
  
## Compression/Decompression
