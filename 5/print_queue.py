debug = True

def validate(rules, update):
	for rule in rules:
		try:
			li = update.index(rule[0])
			ri = update.index(rule[1])
		except ValueError:
			continue
		if li >= ri: # left index always has to be below right index
			if debug:
				print("Update violates rule", rule)
			return False

	return True # passed all tests/rules

if __name__ == "__main__":
	file = open("input.txt", "r")

	# reading rules
	rules = []
	while True:
		line = file.readline()[:-1] # [:-1] to remove \n from end line read
		if line == "":
			break
		rules.append(line.split("|"))
	
	if debug:
		print("Debug: Rules:")
		for rule in rules:
			print(rule)

	# reading updates
	updates = []
	while True:
		line = file.readline()[:-1]
		if line == "":
			break
		updates.append(line.split(","))

	if debug:
		print("Debug: Updates:")
		for update in updates:
			print(update)
		print("Debug: Checking updates...")

	total = 0
	for update in updates:
		valid = validate(rules, update)
		if debug:
			print("{}: {}".format(update, valid))
		
		if valid:
			mi = int(len(update) / 2)
			total += int(update[mi])

	print("Total:", total)