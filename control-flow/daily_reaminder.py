# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        print(f"Reminder: '{task}' is a low priority task.")
    case _:
        print("Reminder: Priority level not recognized.")

# Modify reminder if the task is time-bound
if time_bound == "yes":
    print("That requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")