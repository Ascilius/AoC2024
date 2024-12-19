# hello everybody my name is multiplier

import re

debug = True

def extract_nums(eq):
	nums = re.findall("[0-9]+", eq)
	return nums

if __name__ == "__main__":
	file = open("input.txt", "r")
	string = file.read()

	hits = re.findall("mul\([0-9]+,[0-9]+\)", string)
	
	total = 0
	for hit in hits:
		nums = extract_nums(hit)
		num1 = int(nums[0])
		num2 = int(nums[1])
		total += num1 * num2

	print(total)