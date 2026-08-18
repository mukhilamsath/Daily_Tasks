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
        return Task(data["task_id"], data["title"], data["completed"])


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()                                                                           

    def add_task(self, title):
        if not title.strip():
            print("Task title cannot be empty.")
            return

        task = Task(self.get_next_id(), title)
        self.tasks.append(task)
        print(f"Task {task.task_id} added successfully.")

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} removed successfully.")
                return

        print("Task not found.")

    def mark_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                if task.completed:
                    print("Task is already completed.")
                else:
                    task.mark_done()
                    print(f"Task {task_id} marked as completed.")
                return

        print("Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n========== YOUR TASKS ==========")

        for task in self.tasks:
            status = "DONE" if task.completed else "PENDING"
            print(f"[{status}] {task.task_id}. {task.title}")

        print("================================")

    def get_next_id(self):
        if not self.tasks:
            return 1

        return max(task.task_id for task in self.tasks) + 1

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]

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

            self.tasks = [Task.from_dict(item) for item in data]

        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Warning: tasks.json contains invalid JSON.")
            self.tasks = []
        except IOError as error:
            print("Error loading tasks:", error)
            self.tasks = []


def display_menu():
    print("\n********************************************")
    print("        TO-DO LIST APP")
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
                print("Invalid input.please enter a number.")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark done...: "))
                manager.mark_done(task_id)
            except ValueError:
                print("Invalid input.please enter a number.")

        elif choice == "4":
            manager.view_tasks()

        elif choice == "5":
            manager.save_tasks()
            print("thank you!!!")
            break

        else:
            print("Invalid choice.please select 1-5.")


if __name__ == "__main__":
    main()
