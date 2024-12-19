test_list = ["Geeks for Geeks", "is", "best computer science portal"]

print("The original list: " + str(test_list))

# list comprehension + split()
res = [sub.split() for sub in test_list]

print("THe split strings: " + str(res))