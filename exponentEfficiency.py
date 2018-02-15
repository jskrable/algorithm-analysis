# exponentEfficiency.py
# author: Jack Skrable
# date: 01/29/18
# desc: test algorithm performance for hw problem

import math

# algorithm 1 
# multiplies x and x raised to n-1
def a1(x,n):
	if n == 0:
		y = 1
	else:
		y = x*(x**(n-1))

	print("Algorithm 1 returns", str(y))
	print("Algorithm 2 multiplication count is", str(n))
	
# algorithm 2
# finds an integer m from the log base n of 2
# raises x to the second m times 	
def a2(x,n):
	m = int(math.log(n,2))
	for i in range (0,m):
		x = x**2
	
	print("Algorithm 2 returns", str(x))
	print("Algorithm 2 multiplication count is", str(m+1))

# both algorithms return the same value
# algorithm two is much more efficient
def main():
	print("Please input the parameters")
	x = int(input("x: "))
	n = int(input("n: "))
	a1(x,n)
	a2(x,n)
	
if __name__ == "__main__":
	main()
