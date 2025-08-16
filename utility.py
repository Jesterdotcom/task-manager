def option() -> None:
    options = ("Add task", "Update task", "Delete task", "Mark completed") 
    
    for index, opt in enumerate(options):
        print(f"{index + 1}. {opt}") 
