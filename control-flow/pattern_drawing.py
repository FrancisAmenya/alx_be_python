# Prompt the user for the size of the square they want
size = int(input("Enter the size of the pattern: "))

i = 1
while i < size + 1:
	print("*" * size)
	i += 1
	if i == size:
		break
