#This module contains all your custom made generic_functions

def fill_list(array, character=1, length=10):
	"""Fills a list with a character or number to a specified length"""
	array.append(character)
	for i in array:
		array.append(character)
		if	len(array)	==	length:
			break


def ascii_over_flow(theLetter, theShift):
	theTotal	=	ord(theLetter)	+	theShift
	if theTotal	<	65:
		return ord(theLetter)
	elif	theTotal	>	122:
		return	96	+	theTotal	-	122
	elif	theTotal	<	97:
		return	122	-	(96	-	theTotal)
	else:
		return	theTotal


def enc(passedString, passedShift=10):
	"""pass lower_case strings to encrypt using shift cipher and returns a list"""
	newString	=	[]
	i	=	0
	for letter in passedString:
		newString.append(chr(ascii_over_flow(passedString[i], passedShift)))
		i	=	i	+	1
	return newString
