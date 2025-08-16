print("Welcome User")
print("This Program is to help you manage your daily tasks")

ch0 = input("For adding new tasks please enter Y")
task = open("tasks.txt", "a")

if ch0 in ["Y", "y"]:
    n = int(input("Enter number of tasks you want to add"))
    for i in range(n):
        x = input("Enter the new task :")
        task.writelines(x)
        
ch = input("Do you want to check all task completed if yes enter Y else enter N")
task.close()
task = open("tasks.txt", "a")

if ch in ["Y", "y"]:
    task.truncate(0)
    print("All tasks are cleared now")
task.close()

