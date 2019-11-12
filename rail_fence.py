#This file encrypts text using rail fence transposition.

text	=	input('Enter Plain Text for Rail_Fence_Encryption:\n')
encText	=	[]
y	=	''
fences	=	int(input('Enter number of fences: '))
print(fences)
k	=	fences
l	=	len(text)
print(l)
index	=	0
encText.append(text[0])
while	fences>=0 and fences<l-1:
	index	=	fences
	print('out')
	print(index)
	while	index<=l-1 and index!=0:
#		print(index)
		encText.append(text[index])
#		print(encText)
		index=index+k
#		print(index)
	fences	=fences-1

print(f"\nLength of plain text is {l}\n")
print(f"The plain text \n{text}\n is encrypted as: \n{y.join(encText)}")
