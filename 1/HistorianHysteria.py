debug = True
verbose = False
# stop = 10

# opening file
input_filename = "input.txt"
# input_filename = "test.txt"
input_file = open(input_filename, "r")

# storing left and right nums in respective arrays
left = []
right = []

# reading file and storing numbers
size = 0
while True:
	line = input_file.readline()
	if line == "": # if line is empty, break
		break
	
	if debug:
		print("Debug:", size)
	pair = line.split() # tokenize line
	if debug:
		print(pair)
	left.append(int(pair[0]))
	right.append(int(pair[1]))
	if debug and verbose:
		print(left)
		print(right)
	
	size += 1 # next line

# sorting arrays
left.sort()
right.sort()
if debug and verbose:
	print("Debug: size:", size)
	print("Debug: Sorted arrays:")
	print(left)
	print(right)

# diffing and summing
total = 0
for i in range(size):
	total += abs(left[i] - right[i])

# printing result
print("Result:", total)