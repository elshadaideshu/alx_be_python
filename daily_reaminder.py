task = input("please input a task: ")
priority = input("priority level ( high, medium, low): ")
time_bound = input("is the task time bounded(yes, no): ")
match priority:
    case "high":
        reminder= f "Reminder:{task} has high priority."
    case "medium":
        reminder= f "Reminder:{task} has medium priority"
    case "low":
        reminder= f " Reminder:{task} has low priority."
    case _:
        reminder= "reminder: priority level not recognized"
if time_bound== "yes":
    reminder += "That requires immediate attention today"
print(reminder)
