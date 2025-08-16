from classes import Manager


def option() -> None:
    options = ("List tasks", "Add task", "Update task", "Delete task", "Mark completed","Exit the program")

    print()
    for index, opt in enumerate(options):
        print(f"{index + 1}. {opt}")

    print()


def list(manager: Manager) -> None:
    pend = manager.list().pending()
    if not pend:
        print("No pending tasks")
        return

    print("List of pending tasks:")
    for id, name in pend:
        print(f"{id}. {name}")


def add(manager: Manager) -> None:
    task = input("Enter task name: ")
    manager.add(task)
    print("Task added successfully")


def update(manager: Manager) -> None:
    id = int(input("Enter task id: "))
    if not manager.exists(id):
        print("Task does not exist")
        return

    task = input("Enter task name: ")
    manager.update(id).name(task)
    print("Task updated successfully")


def delete(manager: Manager) -> None:
    id = int(input("Enter task id: "))
    if not manager.exists(id):
        print("Task does not exist")
        return

    manager.delete(id)
    print("Task deleted successfully")


def mark(manager: Manager) -> None:
    id = int(input("Enter task id: "))
    if not manager.exists(id):
        print("Task does not exist")
        return

    manager.update(id).complete()
    print("Task marked as completed")
