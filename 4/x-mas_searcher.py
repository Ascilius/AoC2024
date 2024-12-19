debug = False
verbose = False

# checks whether given coordinate is within table bounds
def valid_coord(si, sj):
	if 0 <= si and si < rows and 0 <= sj and sj <= cols:
		return True
	return False

# searches around A to see if it is at the cross of two MASs
def find_xmas(start):
	# NE
	si = start[0] - 1
	sj = start[1] + 1
	if valid_coord(si, sj):
		if table[si][sj] == "M":
			M = True
		elif table[si][sj] == "S":
			M = False
		else:
			return False
	else:
		return False
	
	# SW
	si = start[0] + 1
	sj = start[1] - 1
	if valid_coord(si, sj):
		if table[si][sj] == "M":
			if M:
				return False
		elif table[si][sj] == "S":
			if not M:
				return False
		else:
			return False
	else:
		return False

	# NW
	si = start[0] - 1
	sj = start[1] - 1
	if valid_coord(si, sj):
		if table[si][sj] == "M":
			M = True
		elif table[si][sj] == "S":
			M = False
		else:
			return False
	else:
		return False
	
	# SE
	si = start[0] + 1
	sj = start[1] + 1
	if valid_coord(si, sj):
		if table[si][sj] == "M":
			if M:
				return False
		elif table[si][sj] == "S":
			if not M:
				return False
		else:
			return False
	else:
		return False

	return True # passed all tests; X-MAS found!

if __name__ == "__main__":
	file = open("input.txt", "r")

	# converting file into 2D char array
	table = []
	while True:
		line = file.readline()
		if len(line) == 0: # reached end of file, break
			break
		table.append(line)

	# iterating through array, finding starting points/directions for XMAS
	rows = len(table)
	cols = len(table[0])
	if debug:
		print("Debug: table:")
		if verbose:
			for line in table:
				print(line, end = "")
		else:
			for i in range(10):
				print(table[i], end = "")
		print("...")
		print("Debug: rows:", rows)
		print("Debug: cols:", cols)

	X_MASs = 0
	for i in range(rows):
		for j in range(cols):
			letter = table[i][j]
			if letter == 'A':
				if debug:
					print("Debug: A found at ({}, {})".format(i, j))
				X_MASs += find_xmas((i, j))

	# printing results :)
	print("X-MASs found:", X_MASs)