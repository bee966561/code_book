#This program decrypts a cipher-text using the words
import generic as g

with open('shiftcrypt.txt') as f:
	contents	=	f.read()

cipherWords	=	contents.split()

