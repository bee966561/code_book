#This program encrypts data using caesar shift cipher. bear in mind that this is a weak encryption algorithm

import generic as g

plainText	=	input('Enter plain text: ')
plainText	=	plainText.lower()
shift	=	int(input('Enter shift'))
encryptedList	=	g.enc(plainText, shift)
encryptedString	=	''
encryptedString	=	encryptedString.join(encryptedList)
with open('shiftcrypt.txt', 'w') as f:
	f.write(encryptedString)

