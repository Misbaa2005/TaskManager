import json

tasks = []

def add_task(title, description):
    tasks.append({"title": title, "description": description, "completed": False})

def edit_task(index, new_title, new_description):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = new_title
        tasks[index]["description"] = new_description

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def mark_task_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def display_tasks():
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i + 1}. {task['title']} [{status}] - {task['description']}")

def save_tasks(filename):
    with open(filename, 'w') as f:
        json.dump(tasks, f)

def load_tasks(filename):
    global tasks
    try:
        with open(filename, 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

def main_menu():
    load_tasks("tasks.json")
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Show Tasks")
        print("6. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == '2':
            display_tasks()
            index = int(input("Enter task number to edit: ")) - 1
            new_title = input("Enter new task title: ")
            new_description = input("Enter new task description: ")
            edit_task(index, new_title, new_description)
        elif choice == '3':
            display_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == '4':
            display_tasks()
            index = int(input("Enter task number to mark as complete: ")) - 1
            mark_task_complete(index)
        elif choice == '5':
            display_tasks()
        elif choice == '6':
            save_tasks("tasks.json")
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
