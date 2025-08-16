from sqlite3 import connect


def option() -> None:
    options = ("Add task", "Update task", "Delete task", "Mark completed") 
    
    for index, opt in enumerate(options):
        print(f"{index + 1}. {opt}") 

class Manager:
    def __init__(self, tableName: str) -> None:
        self.connection = connect(tableName)
        self.cursor = self.connection.cursor()
        self.connection.execute("CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY, name STRING, completed BOOLEAN DEFAULT 0)")

    def exists(self, task: str) -> bool:
        data = self.connection.execute("SELECT * FROM Tasks WHERE name = ?", (task,))
        if data.fetchone():
            return True
        return False

    def getID(self) -> int:
        data = self.connection.execute("SELECT id FROM Tasks")
        if data.fetchall():
            return data[-1]
        return 1

    def add(self, task: str) -> None:
        self.connection.execute("INSERT INTO Tasks(id, name) VALUES(?, ?)", (self.getID(), task))
        self.connection.commit()
