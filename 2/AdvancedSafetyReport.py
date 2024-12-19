debug = False

filename = "input.txt"
file = open(filename, "r")

def check_report(levels):
	safe = True
	index = -1
	size = len(levels)
	direction = 0
	for i in range(1, size):
		diff = int(levels[i]) - int(levels[i-1])

		# checking difference
		if diff == 0 or abs(diff) > 3:
			safe = False
			index = i
			break

		# changing direction
		if i == 1:
			direction = diff / abs(diff)
		else:
			curr_dire = diff / abs(diff)
			if direction != curr_dire: # if direction changes, levels are unsafe
				safe = False
				index = i
				break
	results = [safe, index]
	return results

total_reports = 0
safe_reports = 0
while True:
	line = file.readline()
	if line == "":
		break
	total_reports += 1

	levels = line.split()
	print(levels)

	results = check_report(levels)
	safe = results[0]
	index = results[1]

	if safe:
		safe_reports += 1
		print("Result: Safe")
	else:
		safe = False
		for i in range(len(levels)):
			pared_levels = levels.copy()
			pared_levels.pop(i)
			results = check_report(pared_levels)
			print("{}: {}".format(pared_levels, results[0]))
			if results[0]:
				safe = True
				break

		if safe:
			safe_reports += 1
			print("Result: Safe")
		else:
			print("Result: Unsafe")

		"""
		left = levels.copy()
		right = levels.copy()
		# tolerance of one unsafe level, removing either level at unsafe change
		left.pop(index-1)
		right.pop(index)

		# check again
		left_result = check_report(left)
		right_result = check_report(right)
		print("Removed {} at index {}: {}".format(levels[index-1], index-1, left_result[0]))
		print("Removed {} at index {}: {}".format(levels[index], index, right_result[0]))
		if left_result[0] or right_result[0]:
			safe_reports += 1
			print("Result: Safe")
		else:
			print("Result: Unsafe")
		"""

	if debug:
		input()

print("Total reports:", total_reports)
print("Safe Reports:", safe_reports)