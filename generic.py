#This module contains all your custom made generic_functions

def fill_list(array, character=1, length=10):
	"""Fills a list with a character or number to a specified length"""
	array.append(character)
	for i in array:
		array.append(character)
		if	len(array)	==	length:
			break

