debug = False
verbose = False

file = open("input.txt", "r")

# checks whether given coordinate is within table bounds
def valid_coord(si, sj):
	if 0 <= si and si < rows and 0 <= sj and sj <= cols:
		return True
	return False

# searches in the specified direction for an XMAS
def find_xmas(start, direct):
	si = start[0] + direct[0]
	sj = start[1] + direct[1]
	if not valid_coord(si, sj) or table[si][sj] != 'M':
		return False
	
	si += direct[0]
	sj += direct[1]
	if not valid_coord(si, sj) or table[si][sj] != 'A':
		return False

	si += direct[0]
	sj += direct[1]
	if not valid_coord(si, sj) or table[si][sj] != 'S':
		return False

	return True # passed all tests; XMAS found!

# start search queries in every direction
def search_around(start):
	E = find_xmas(start, (0,1))
	NE = find_xmas(start, (-1,1))
	N = find_xmas(start, (-1,0))
	NW = find_xmas(start, (-1,-1))
	W = find_xmas(start, (0,-1))
	SW = find_xmas(start, (1,-1))
	S = find_xmas(start, (1,0))
	SE = find_xmas(start, (1,1))
	total = E + NE + N + NW + W + SW + S + SE 
	
	if debug:
		if verbose:
			print("\tE:", E)
			print("\tNE:", NE)
			print("\tN:", N)
			print("\tNW:", NW)
			print("\tW:", W)
			print("\tSW:", SW)
			print("\tS:", S)
			print("\tSE:", SE)
		print("\tTotal found:", total)

	return total

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

XMASs = 0
for i in range(rows):
	for j in range(cols):
		letter = table[i][j]
		if letter == 'X':
			if debug:
				print("Debug: X found at ({}, {})".format(i, j))
			XMASs += search_around((i, j))

# printing results :)
print("XMASs found:", XMASs)