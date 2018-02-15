# maxSort.py
# author: Jack Skrable
# date: 02/11/18
# desc: test algorithm comparison for hw problem

def main():

	# declare variables
	E = []
	counter = 0
	
	# choose file to sort
	filename = "testData1.txt"
	# read lines from file into list
	file = open(filename, "r")
	for line in file:
		E.append(int(line))
	# print unsorted list
	print(E)
	
	# loop through list
	for i in range(len(E)):
		# slice array to get unsorted
		unsorted = E[i:len(E)]
		# end if unsorted is empty
		if not unsorted:
			break 
		# else pop max from unsorted off test and insert in front
		else: 
			E.insert(0,E.pop(unsorted.index(max(unsorted))+i))
			counter+=1
	# print sorted list and swap counter 
	print(E)
	print(counter)
	print(len(E))

if __name__ == "__main__":
	main()
