debug = True
verbose = False

# parsing and calculating eq, checking with sol
def calculate(sol, eq):
	org = eq.copy()

	# first pass (*)
	i = 1
	while i < len(eq):
		if eq[i] == '*':
			n2 = eq.pop(i+1)
			eq.pop(i)
			n1 = eq.pop(i-1)

			n = n1 * n2

			eq.insert(i-1, n)
			if debug and verbose:
				print("\t\tDebug: new eq:", eq)

			i -= 2
		i += 2

	# second pass (+)
	i = 1
	while i < len(eq):
		if eq[i] == '+':
			n2 = eq.pop(i+1)
			eq.pop(i)
			n1 = eq.pop(i-1)

			n = n1 + n2

			eq.insert(i-1, n)
			if debug and verbose:
				print("\t\tDebug: new eq:", eq)

			i -= 2
		i += 2

	result = eq[0] == sol
	if result and debug:
		print("\tDebug: Valid equation found:", org)
		# input()
	return result

# recursive checking by generating equations with given nums
def check(sol, eq, i):
	if i >= len(eq):
		if debug and verbose:
			print("\tDebug: Calculating \"{}\":".format(eq))
		return calculate(sol, eq)

	valid = False

	eq1 = eq.copy()
	eq1[i] = "+"
	if debug and verbose:
		print("\tDebug: eq1:", eq1)
		# input()
	valid = valid or check(sol, eq1, i+2)
	
	eq2 = eq.copy()
	eq2[i] = "*"
	if debug and verbose:
		print("\tDebug: eq2:", eq2)
		# input()
	valid = valid or check(sol, eq2, i+2)

	return valid

if __name__ == "__main__":
	# parsing inputs
	filename = "input.txt"
	print("Checking \"{}\"...".format(filename))
	file = open(filename, "r")
	valid = 0
	while True:
		line = file.readline()
		if line == "":
			break
		line = line[:-1] # removing ending \n
		toks = line.split(": ")
		if debug:
			print("\nDebug: line:", line)
			print("Debug: split line:", toks)
		
		# getting solution and numbers
		sol = int(toks[0])
		nums = toks[1].split(" ")
		if debug:
			print("Debug: sol:", sol)
			print("Debug: nums:", nums)
		
		# generating blank equation
		n = len(nums) * 2 - 1
		eq = []
		for i in range(n):
			if i % 2 == 0:
				eq.append(int(nums[int(i/2)]))
			else:
				eq.append("")
		if debug:
			print("Debug: eq:", eq)

		# finding valid equation
		if check(sol, eq, 1):
			valid += 1

	# results
	print("Calibration Result:", valid)