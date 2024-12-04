debug = True

filename = "input.txt"
file = open(filename, "r")

safe = 0
while True:
	line = file.readline()
	if line == ""
		break

	levels =  line.split()
	if debug:
		print(levels)

	safe += 1 # assume levels are safe, checking below
	size = len(levels)
	direction = 0
	for i in range(1, size):
		diff = levels[i] - levels[i-1]

		# checking difference
		if diff == 0 or abs(diff) > 3:
			safe -= 1
			break

		# changing direction
		if i == 1:
			direction = diff / abs(diff)
		else:
			curr_dire = diff / abs(diff)
			if direction != curr_dire: # if direction changes, levels are unsafe
				safe -= 1
				break