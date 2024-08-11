import json

TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({'description': description, 'due_date': due_date, 'completed': False})
    save_tasks(tasks)

def view_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{i + 1}. {task['description']} (Due: {task['due_date']}) - {status}")

def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = not tasks[task_number]['completed']
        save_tasks(tasks)

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
