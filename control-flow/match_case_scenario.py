# Prompt the user to enter the numbers and operator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator_ = input("Choose the operation (+, -, *, /): ")
match operator_:
	case "+":
		result_ = num1 + num2
	case "-":
		result_ = num1 - num2
	case "*":
		result_ = num1 * num2
	case "/":
		result_ = num1 / num2

# Providing a result
print(f"The result is {result_}.")
