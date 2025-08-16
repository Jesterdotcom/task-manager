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
        functions.list(manager)
        functions.add(manager)

    elif n == 3:
        functions.list(manager)
        functions.update(manager)

    elif n == 4:
        functions.list(manager)
        functions.delete(manager)

    elif n == 5:
        functions.list(manager)
        functions.mark(manager)

    elif n == 6:
        print("Goodbye")
        break

    else:
        print("Invalid option")

