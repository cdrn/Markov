# IMPORTS #
from random import *
from sys import *
from collections import defaultdict


#dummy var TODO delet this
var = 0;


class Markov_Chain:
	#global data structure which will hold the chain
	global markov_chain 
	markov_chain = defaultdict(list)

	def create_markov(self, fileInput):
		# open and parse the text file
		open_input = open(fileInput, 'r')
		# pass it to a string
		input_string = open_input.read()
		#split into an array
		words = input_string.split()
		#print the split array for debugging
		# print(words)

		#store a list of subsequents in each dictionary word entry
		for i, word in enumerate(words):
				# try append next to dictionary if a next word exists
			try:
				markov_chain[word].append(words[i+1])
			except:
				print "hmmm some error occured"
		print(markov_chain)

	def create_output(self, length):
		#if input length is zero, create a random length
		if length == 0:
			length = randint(1, 50)

		outputString = "OUTPUT STRING: "
		outputString += str(choice(list(markov_chain)))

		for word in range(length):

			# split the new string every time we iterate, by spaces
			parseOutput = outputString.split()
			#store the last word in the markov chain here to search for the next word (key)
			lastWord = parseOutput[-1]
			try:
				#use the key in the markov chain to retrieve possible next words
				keyList = markov_chain[lastWord]
				#save length of keylist, decrement by 1 for 0 indexing
				keyListLen = len(keyList)-1
				keyListRand = randint(0, keyListLen)
				#select a word from the keylist and add to the output string
				outputString += " " + keyList[keyListRand]
			except:
				print 'no match for iteration', word

		print(outputString)




newchain = Markov_Chain()

newchain.create_markov("test.txt")

newchain.create_output(20)




