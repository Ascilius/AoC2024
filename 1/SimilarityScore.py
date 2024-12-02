debug = True
verbose = True

# opening file
input_filename = "input.txt"
input_file = open(input_filename, "r")

# storing nums and num counts in a dict
left = []
right = {}

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
	i = int(pair[1])
	try:
		right[i] += 1
	except:
		right[i] = 1
	if debug and verbose:
		print(left)
		print(right)
	
	size += 1 # next line
if debug and verbose:
	print("Debug: size:", size)
	print(left)
	print(right)

# diffing and summing
score = 0
for num in left:
	try:
		score += num * right[num]
	except:
		if debug:
			print("Debug:", num, "not found!")

# printing result
print("Result:", score)