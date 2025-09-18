# Prompt the user for the number's table they want
num = int(input("Enter a number to see its multiplication table: "))

for i in range(1,11):
	if i > 10:
		break

	result = i * num
	print(f"{num} * {i} = {result}")
