task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
        print(reminder)
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
        print(reminder)
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
        print(reminder)
    case _:
        print(f"Task: {task} priority not specified")
    
if time_bound == "yes":
    print("It is time-sensitive and requires immediate attention today!")
else:
    print("no time constraint")