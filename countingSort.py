# countingSort.py
# author: Jack Skrable
# date: 03/08/18
# desc: test counting sort for study

def main():

	# test array
	A = [0,2,5,2,4,6,7,2,7,8,1,2,3]
	print("To sort: " + str(A))
	# get highest value
	m = max(A)
	# create empty counter array
	c  = [0] * (m+1)
	# for each value in array, add values counts
	for i in A:
		c[i] += 1
	print("Counter: " + str(c))
	# empty index variable for swapping
	index = 0
	# loop through counter array
	for i in range(len(c)):
		# until over
		while 0 < c[i]:
			# swap index's place in A
			A[index] = i
			# go to next index
			index += 1
			# decrement counter array
			c[i] -= 1
	# print sorted array	
	print("Sorted: " + str(A))
if __name__ == "__main__":
	main()