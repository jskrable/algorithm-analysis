# doubleHashing.py
# author: Jack Skrable
# date: 03/13/18
# desc: test double hash for study

import math

def main():

	m = 11
	k = input("K=")
	
	def h1(k,m):
		return int(k%m)
		
	def h2(k,m):
		return int(1+k%(m-1))

	def h():
		int(h1(k,m))+int(h2(k,m))
	
	print(h())
		
if __name__ == "__main__":
	main()