debug = True

def check_next(lab, gr, gc, dr, dc):
	nr = gr + dr
	nc = gc + dc

	n = lab[nr][nc]
	if debug:
		print("\t({},{}): {}".format(nr, nc, n))
	if n == '#':
		return False
	return True

def turn(dr, dc):
	if debug:
		print("\tTurning...")
	if dr == 0:
		if dc == -1:
			ndr = -1
		elif dc == 1:
			ndr = 1
		ndc = 0
	elif dc == 0:
		if dr == -1:
			ndc = 1
		elif dr == 1:
			ndc = -1
		ndr = 0
	if debug:
		print("\tNew direction: ({},{})".format(ndr, ndc))
	return (ndr, ndc)

if __name__ == "__main__":
	file = open("input.txt", "r")
	
	lab = []
	rows = -1
	cols = -1
	gr = -1 # starting row of the guard
	gc = -1
	while True:
		line = file.readline()[:-1]
		if line == "":
			break
		rows += 1
		lab.append(line)
		temp = line.find('^')
		if temp != -1:
			if gc != -1:
				print("Warning: Guard found twice")
			gr = rows
			gc = temp
			cols = len(line)

	if debug:
		print("Debug: Lab map ({} x {}):".format(rows, cols))
		for row in lab:
			print(row)
		print("Debug: Guard starting location: row {}, col {}".format(gr, gc))

	# pathfinding
	visited = set()
	dr = -1
	dc = 0
	while 0 <= gr and gr < rows and 0 <= gc and gc < cols: # TOFIX
		if debug:
			print("Debug: ({},{}):".format(gr,gc))
			print("\tCurrent direction: ({},{}):".format(dr, dc))
		
		# saving
		visited.add((gr,gc))

		# checking
		while not check_next(lab, gr, gc, dr, dc):
			nd = turn(dr, dc)
			dr = nd[0]
			dc = nd[1]

		# moving
		gr += dr
		gc += dc

	# counting unique positions
	print("Unique positions:", len(visited))