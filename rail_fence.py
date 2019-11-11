#This file encrypts text using rail fence transposition.

text	=	'The quick brown fox jumped over the lazy dog and killed it'
l	=	len(text)
print(f"\nLength of plain text is {l}\n")
encText	=	[]
y	=	''
index	=	0
a	=	0
while	a!=2:
	encText.append(text[index])
	index+=2
	if index>=l-1:
		index=1
		a	+=	1

print(f"The plain text \n{text}\n is encrypted as \n{y.join(encText)}")
