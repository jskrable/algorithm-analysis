# exponent_efficiency.py
# author: Jack Skrable
# date: 01/29/18
# desc: test algorithm performance for hw problem

import math

def a1(x,n):
	if n == 0:
		y = 1
	else:
		y = x*(x**(n-1))

	print("Algorithm 1 returns", str(y))
	print("Algorithm 2 multiplication count is", str(n))
	
def a2(x,n):
	m = int(math.log(n,2))
	for i in range (0,m):
		x = x**2
	
	print("Algorithm 2 returns", str(x))
	print("Algorithm 2 multiplication count is", str(m+1))
	
def main():
	print("Please input the parameters")
	x = int(input("x: "))
	n = int(input("n: "))
	a1(x,n)
	a2(x,n)
	
if __name__ == "__main__":
	main()
