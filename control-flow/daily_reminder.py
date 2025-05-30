task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        priority_text = "HIGH"
    case "medium":
        priority_text = "MEDIUM"
    case "low":
        priority_text = "LOW"
    case _:
        print(f"Task: '{task}' has an invalid priority. Please enter high, medium, or low.")
        exit()

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} priority task that requires immediate attention today!")
else:
    print(f"Reminder: '{task}' is a {priority_text} priority task (no time constraint).")