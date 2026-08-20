import json


class Task:
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data.get("completed", False)
        )


class TaskManager:
    def __init__(self, filename="tasks1.json"):
        self.filename = filename
        self.tasks = {}
        self.load_tasks()

    def add_task(self, title):
        if not title.strip():
            print("Task title cannot be empty.")
            return

        task_id = len(self.tasks) + 1

        task = Task(task_id, title)

        self.tasks[task_id] = task

        print(f"Task {task_id} added successfully.")

    def remove_task(self, task_id):
        if task_id not in self.tasks:
            print("Task not found.")
            return

        del self.tasks[task_id]

        self.renumber_tasks()

        print(f"Task {task_id} removed successfully.")

    def renumber_tasks(self):
        new_tasks = {}

        new_id = 1

        for task in self.tasks.values():
            task.task_id = new_id
            new_tasks[new_id] = task
            new_id += 1

        self.tasks = new_tasks

    def mark_done(self, task_id):
        if task_id in self.tasks:
            task = self.tasks[task_id]

            if task.completed:
                print("Task is already completed.")
            else:
                task.mark_done()
                print(f"Task {task_id} marked as completed.")

        else:
            print("Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n********* YOUR TASKS *********")

        for task_id, task in self.tasks.items():
            status = "DONE" if task.completed else "PENDING"

            print(f"[{status}] {task_id}. {task.title}")

        print("================================")

    def save_tasks(self):
        data = [
            task.to_dict()
            for task in self.tasks.values()
        ]

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

            print("Tasks saved successfully.")

        except IOError as error:
            print("Error saving tasks:", error)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            self.tasks = {
                item["task_id"]: Task.from_dict(item)
                for item in data
            }

            self.renumber_tasks()

        except FileNotFoundError:
            self.tasks = {}

        except json.JSONDecodeError:
            print("Warning: tasks.json contains invalid JSON.")
            self.tasks = {}

        except IOError as error:
            print("Error loading tasks:", error)
            self.tasks = {}


def display_menu():
    print("\n********************************************")
    print("              TO-DO LIST APP")
    print("********************************************")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Done")
    print("4. View Tasks")
    print("5. Exit")
    print("********************************************")


def main():
    manager = TaskManager()

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            manager.add_task(title)

        elif choice == "2":
            try:
                task_id = int(input("Enter task id to remove: "))
                manager.remove_task(task_id)

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark done: "))
                manager.mark_done(task_id)

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            manager.view_tasks()

        elif choice == "5":
            manager.save_tasks()
            print("Thank you!!!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()