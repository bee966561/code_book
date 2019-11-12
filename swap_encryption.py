#This program encrypts text using swap_encryption algorithm

#This algorithm can be used to decrypt swap_encryption too. Just pass the cipher text and Voila

import generic as g

aStore	=	[]
plainText	=	input('Enter plain text for encryption:::\n')
l	=	len(plainText)
if	l	%	2	==	0:
	p	=	2
else:
	p	=	1
g.fill_list(aStore,1,l)
i	=	0
out	=	''
for letter in plainText:
#	print(f"i before increment:{i}")
#	print(f"index before increment:{i+((-1)**i)}")
	if	i	==	l-p:
		aStore[l-p:]	=	plainText[l-p:]
		break
	aStore[i+((-1)**i)]	=	letter
	i	=	i	+	1
#	print(f"i after increment:{i}")
#	print(f"index after increment{i+((-1)**i)}")
print(f"The encrypted text is:\n {out.join(aStore)}")
#print(aStore)
