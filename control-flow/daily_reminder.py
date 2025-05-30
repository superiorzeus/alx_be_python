# task = input("Enter your task: ")
# priority = input("Priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

# match priority:
#     case "high":
#         reminder = f"Reminder: '{task}' is a HIGH priority task."
#         print(reminder)
#     case "medium":
#         reminder = f"Reminder: '{task}' is a MEDIUM priority task."
#         print(reminder)
#     case "low":
#         reminder = f"Reminder: '{task}' is a LOW priority task."
#         print(reminder)
#     case _:
#         print(f"Task: {task} priority not specified")
    
# if time_bound == "yes":
#     print("It is time-sensitive and requires immediate attention today!")
# else:
#     print("no time constraint")

# task = input("Enter your task: ")
# priority = input("Priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

# match priority:
#     case "high":
#         reminder = f"Reminder: '{task}' is a HIGH priority task"
#     case "medium":
#         reminder = f"Reminder: '{task}' is a MEDIUM priority task"
#     case "low":
#         reminder = f"Reminder: '{task}' is a LOW priority task"
#     case _:
#         print(f"Task: '{task}' has an invalid priority. Please enter high, medium, or low.")
#         exit()

# # Add time sensitivity message
# if time_bound == "yes":
#     reminder += " that requires immediate attention today!"
# else:
#     reminder += " (no time constraint)"

# # Final customized reminder
# print(reminder)

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

# Construct the full reminder in one line
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} priority task that requires immediate attention today!")
else:
    print(f"Reminder: '{task}' is a {priority_text} priority task (no time constraint).")