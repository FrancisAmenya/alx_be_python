# Prompt the user for the size of the square they want
size = int(input("Enter size of the pattern: "))

for i in range(1, size+1):
	if i > size:
		break
	print("*" * size)

