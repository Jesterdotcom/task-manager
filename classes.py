from sqlite3 import Connection, connect


class List:
    def __init__(self, tasks: list[tuple[int, str, int]]) -> None:
        self.tasks = tasks

    def pending(self) -> list[tuple[int, str]]:
        pend = []
        for id, name, completed in self.tasks:
            if completed == 0:
                pend.append((id, name))

        return pend

    def completed(self) -> list[tuple[int, str]]:
        comp = []
        for id, name, completed in self.tasks:
            if completed == 0:
                comp.append((id, name))

        return comp


class Update:
    def __init__(self, connection: Connection, id: int) -> None:
        self.connection = connection
        self.id = id

    def name(self, task: str) -> None:
        self.connection.execute(
            "UPDATE Tasks SET name = ? WHERE id = ?", (task, self.id)
        )
        self.connection.commit()

    def complete(self) -> None:
        self.connection.execute(
            "UPDATE Tasks SET completed = ? WHERE id = ?", (1, self.id)
        )
        self.connection.commit()


class Manager:
    def __init__(self, tableName: str) -> None:
        self.connection = connect(tableName)
        self.cursor = self.connection.cursor()
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY, name STRING, completed BOOLEAN DEFAULT 0)"
        )

    def exists(self, id: int) -> bool:
        data = self.connection.execute("SELECT * FROM Tasks WHERE id = ?", (id,))
        if data.fetchone():
            return True
        return False

    def _getNextID(self) -> int:
        data = self.connection.execute("SELECT id FROM Tasks")
        if item := data.fetchall():
            return item[-1][0] + 1
        return 1

    def add(self, task: str) -> None:
        self.connection.execute(
            "INSERT INTO Tasks(id, name) VALUES(?, ?)", (self._getNextID(), task)
        )
        self.connection.commit()

    def list(self) -> List:
        data = self.connection.execute("SELECT * FROM Tasks")
        return List(data.fetchall())

    def delete(self, id: int) -> None:
        self.connection.execute("DELETE FROM Tasks WHERE id = ?", (id,))
        self.connection.commit()

    def update(self, id: int) -> Update:
        return Update(self.connection, id)
