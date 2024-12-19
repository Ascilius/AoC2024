debug = False

filename = "input.txt"
file = open(filename, "r")

safe_reports = 0
while True:
	line = file.readline()
	if line == "":
		break

	levels =  line.split()
	print(levels)

	safe = True
	size = len(levels)
	direction = 0
	for i in range(1, size):
		diff = int(levels[i]) - int(levels[i-1])

		# checking difference
		if diff == 0 or abs(diff) > 3:
			safe = False
			break

		# changing direction
		if i == 1:
			direction = diff / abs(diff)
		else:
			curr_dire = diff / abs(diff)
			if direction != curr_dire: # if direction changes, levels are unsafe
				safe = False
				break

	if safe:
		safe_reports += 1
		print("Result: Safe")
	else:
		print("Result: Unsafe")

	if debug:
		input()

print("Safe Reports:", safe_reports)