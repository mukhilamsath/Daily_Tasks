import json
from collections import deque


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
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = {}
        self.deleted_ids = deque()
        self.next_id = 1
        self.load_tasks()

    def add_task(self, title):
        if not title.strip():
            print("Task title cannot be empty.")
            return

        if self.deleted_ids:
            task_id = self.deleted_ids.popleft()
        else:
            task_id = self.next_id
            self.next_id += 1

        task = Task(task_id, title)

        self.tasks[task_id] = task

        print(f"Task {task_id} added successfully.")

    def remove_task(self, display_id):
        task_id = self.get_task_id(display_id)

        if task_id is not None:
            del self.tasks[task_id]

            self.deleted_ids.append(task_id)

            print(f"Task {display_id} removed successfully.")
        else:
            print("Task not found.")

    def mark_done(self, display_id):
        task_id = self.get_task_id(display_id)

        if task_id is not None:
            task = self.tasks[task_id]

            if task.completed:
                print("Task is already completed.")
            else:
                task.mark_done()
                print(f"Task {display_id} marked as completed.")
        else:
            print("Task not found.")

    def get_task_id(self, display_id):
        sorted_tasks = sorted(
            self.tasks.values(),
            key=lambda task: task.task_id
        )

        if 1 <= display_id <= len(sorted_tasks):
            return sorted_tasks[display_id - 1].task_id

        return None

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n********* YOUR TASKS *********")

        sorted_tasks = sorted(
            self.tasks.values(),
            key=lambda task: task.task_id
        )

        display_id = 1

        for task in sorted_tasks:
            status = "DONE" if task.completed else "PENDING"

            print(f"[{status}] {display_id}. {task.title}")

            display_id += 1

        print("================================")

    def save_tasks(self):
        data = {
            "next_id": self.next_id,
            "deleted_ids": list(self.deleted_ids),
            "tasks": [
                task.to_dict()
                for task in self.tasks.values()
            ]
        }

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

            self.next_id = data.get("next_id", 1)

            self.deleted_ids = deque(
                data.get("deleted_ids", [])
            )

            task_data = data.get("tasks", [])

            self.tasks = {
                item["task_id"]: Task.from_dict(item)
                for item in task_data
            }

        except FileNotFoundError:
            self.tasks = {}
            self.deleted_ids = deque()
            self.next_id = 1

        except json.JSONDecodeError:
            print("Warning: tasks.json contains invalid JSON.")

            self.tasks = {}
            self.deleted_ids = deque()
            self.next_id = 1

        except IOError as error:
            print("Error loading tasks:", error)

            self.tasks = {}
            self.deleted_ids = deque()
            self.next_id = 1


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