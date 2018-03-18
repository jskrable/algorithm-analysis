# randomLists.py
# author: Jack Skrable
# date: 02/12/18
# desc: generate random lists of 100 integers

from random import randint
import os

def main():

	data = []
	entry = 0
	handler = open("testData6.txt", "w")	

	for i in range (100,0,-1):
		#entry = str(randint(0,100)) + '\n'
		entry = str(i) + '\n'
		handler.write(entry)

	handler.close()

if __name__ == "__main__":
	main()