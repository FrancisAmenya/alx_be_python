# Prompt the user to enter their monthly income and expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculating the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projecting yearly savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Printing the user's monthly and yearly savings in the format
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
