task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task",end=" ")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task",end=" ")
    case "low":
        print(f"Reminder: '{task}' is a low priority task",end=" ")
    case _:
        print("Reminder: Priority level not recognized.")
if time_bound == "yes":
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")