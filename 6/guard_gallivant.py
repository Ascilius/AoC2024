debug = True

if __name__ == "__main__":
	file = open("input.txt", "r")
	
	lab = []
	while True:
		line = file.readline()[:-1]
		if line == "":
			break
		lab.append(line)

	if debug:
		for row in lab:
			print(row)