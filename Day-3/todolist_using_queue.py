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

    def __init__(self, filename="tasks1.json"):
        self.filename = filename

        
        self.tasks = {}

      
        self.task_order = deque()

        self.next_id = 1

        self.load_tasks()

    def add_task(self, title):

        if not title.strip():
            print("Task title cannot be empty.")
            return

        task_id = self.next_id

        task = Task(task_id, title)

        self.tasks[task_id] = task
        self.task_order.append(task_id)

        self.next_id += 1

        print(f"Task {len(self.task_order)} added successfully.")

    def remove_task(self, task_id):

        if task_id < 1 or task_id > len(self.task_order):
            print("Task not found.")
            return

       
        actual_id = self.task_order[task_id - 1]

        del self.tasks[actual_id]

        self.task_order.remove(actual_id)

        print(f"Task {task_id} removed successfully.")

    def mark_done(self, task_id):

        if task_id < 1 or task_id > len(self.task_order):
            print("Task not found.")
            return

       

        actual_id = self.task_order[task_id - 1]

        task = self.tasks[actual_id]

        if task.completed:
            print("Task is already completed.")

        else:
            task.mark_done()
            print(f"Task {task_id} marked as completed.")

    def view_tasks(self):

        if not self.task_order:
            print("\nNo tasks available.")
            return

        print("\n********* YOUR TASKS *********")

        display_id = 1

        for actual_id in self.task_order:

            task = self.tasks[actual_id]

            status = "DONE" if task.completed else "PENDING"

            print(f"[{status}] {display_id}. {task.title}")

            display_id += 1

        print("================================")

    def save_tasks(self):

        data = [
            self.tasks[task_id].to_dict()
            for task_id in self.task_order
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

            self.tasks = {}
            self.task_order = deque()

            for item in data:

                task = Task.from_dict(item)

                self.tasks[task.task_id] = task
                self.task_order.append(task.task_id)

            if self.tasks:
                self.next_id = max(self.tasks.keys()) + 1

        except FileNotFoundError:

            self.tasks = {}
            self.task_order = deque()

        except json.JSONDecodeError:

            print("Warning: tasks.json contains invalid JSON.")

            self.tasks = {}
            self.task_order = deque()

        except IOError as error:

            print("Error loading tasks:", error)

            self.tasks = {}
            self.task_order = deque()


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

                task_id = int(
                    input("Enter task id to remove: ")
                )

                manager.remove_task(task_id)

            except ValueError:

                print("Invalid input. Please enter a number.")

        elif choice == "3":

            try:

                task_id = int(
                    input("Enter task ID to mark done: ")
                )

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