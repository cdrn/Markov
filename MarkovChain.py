# IMPORTS #
from random import *
from sys import *

var = 0;



def create_markov(input):
	# create a "list" in python to store the markov chain (it's an array). This will house the markov chain.
	markov_chain = []

	# open and parse the text file
	open_input = open('test.txt', 'r')
	# pass it to a string
	input_string = open_input.read()
	#split into an array
	words = input_string.split()
	#print the split array for debugging
	print(words)


create_markov(var)






