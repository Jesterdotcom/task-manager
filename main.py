import functions
from classes import Manager

manager = Manager("database.db")

print("Welcome to your task manager")

while True:
    functions.option()
    try:
        n = int(input("Enter your option: "))
    except ValueError:
        print("Invalid option")
        continue

    if n == 1:
        functions.list(manager)

    elif n == 2:
        functions.add(manager)
        functions.list(manager)

    elif n == 3:
        functions.update(manager)
        functions.list(manager)

    elif n == 4:
        functions.delete(manager)
        functions.list(manager)

    elif n == 5:
        functions.mark(manager)
        functions.list(manager)

    elif n == 6:
        print("Goodbye")
        break

    else:
        print("Invalid option")
