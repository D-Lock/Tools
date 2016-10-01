# Tools
Merging, Splitting and Encrypting Tools for D-Lock
## Encryption
crypt_sys uses AES encryption to block cipher the binary file that is chosen and outputs the result to a file

   Syntax:
  - [-e|-d] [inputfile] [outputfile] [password that is exactly 16 characters]
  - e: encrypts the input file with AES that is salted from the password and random number generation from the Python Crypto package
  - d: decrypts the input file with AES from the password given and returns the file to the output filename/pathname specificied.
  
  The password needs to be 16 characters, and preferred to have capitals, special characters under ASCII and  numbers for security purposes.
  
## Compression/Decompression
press-sys is the tool used to compress and decompress encrypted files on the client side of the stack. This tool is only used client side and used to before encryption for reducing file size and data transfer
 
 Syntax:
  - [-c|-d] [inputfile] [-o] [outputfile]
  - c: compress the input file specified directly using the zip toolkit using standard compression rate of m5
  - d: decompresses the input file specified into the out output file.
