# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder_a = "'" + task + "'"
reminder_no = ". Consider completing it when you have free time."
reminder_yes = " that requires immediate attention today!"

priority_high = " is a high priority task"
priority_medium = " is a medium priority task"
priority_low = " is a low priority task"

match priority:
	case "high":
		reminder_a = reminder_a + priority_high
	case "low":
		reminder_a = reminder_a + priority_low
	case "medium":
		reminder_a = reminder_a + priority_medium

if time_bound == "yes":
	print(f"'Reminder: ' + {reminder_a} + {reminder_yes}")
elif time_bound == "no":
        print(f"'Note: ' + {reminder_a} + {reminder_no}")
