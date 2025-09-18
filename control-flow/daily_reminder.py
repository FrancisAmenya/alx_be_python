# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder_a = "'" + task + "'"
reminder_no = ". Consider completing it when you have free time."
reminder_yes = " that requires immediate attention today!"
reminder_b = ""
reminder_c = ""
reminder_d = "Note: "
reminder_e = "Reminder: "

priority_high = " is a high priority task"
priority_medium = " is a medium priority task"
priority_low = " is a low priority task"

match priority:
	case "high":
		reminder_b = reminder_a + priority_high
	case "low":
		reminder_b = reminder_a + priority_low
	case "medium":
		reminder_b = reminder_a + priority_medium

if time_bound == "yes":
	reminder_c = reminder_e + reminder_b + reminder_yes
elif time_bound == "no":
	reminder_c = reminder_d + reminder_b + reminder_no

print(f"{reminder_c}")
