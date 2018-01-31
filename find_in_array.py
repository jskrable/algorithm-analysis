# find_in_array.py
# author: Jack Skrable
# date: 01/30/18
# desc: test algorithm comparison for hw problem

def main():

	# get search number
	k = int(input("Choose a number to search for: "))
	# initialize ordered array
	l = []
	# initialize comparison counter
	counter = 0
	
	# populate sample ordered array
	for i in range(100):
		l.append(i)

	# loop through array in increments of 4
	for j in range(0, len(l), 4):
		# increment counter each <= check
		counter += 1
		if k <= l[j]:
			# if ==, inc. counter and end
			if k == l[j]:
				counter += 1
				print("Found! Your number was ", k)
				print("Counter: ", counter)
				break
			# else loop through 3 preceding values
			else:
				for m in range(l[j-3],l[j]):
					# inc. counter for each == check
					counter += 1
					# if ==, inc. counter and end
					if k == l[m]:
						print("Found! Your number was ", k)
						print("Counter: ", counter)
						break

if __name__ == "__main__":
	main()