import re

debug = True

def extract_nums(eq):
	nums = re.findall("[0-9]+", eq)
	return nums

if __name__ == "__main__":
	file = open("input.txt", "r")
	string = file.read()

	hits = re.findall("mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", string)
	print(hits)

	total = 0
	do = True
	for hit in hits:
		if len(hit) == 4: # do()
			do = True
		elif len(hit) == 7: # don't()
			do = False
		elif do:
			nums = extract_nums(hit)
			num1 = int(nums[0])
			num2 = int(nums[1])
			total += num1 * num2

	print(total)