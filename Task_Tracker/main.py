import json
import hashlib
import os

USER_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

def register():
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter new password: ")
    users[username] = hash_password(password)
    save_users(users)
    print("Registration successful!")

def login():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == hash_password(password):
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None
    

def get_task_file(username):
    return f"tasks_{username}.json"

def load_tasks(username):
    file = get_task_file(username)
    if not os.path.exists(file):
        return []
    with open(file, 'r') as f:
        return json.load(f)

def save_tasks(username, tasks):
    file = get_task_file(username)
    with open(file, 'w') as f:
        json.dump(tasks, f)


def add_task(username):
    tasks = load_tasks(username)
    desc = input("Enter task description: ")
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": desc, "status": "Pending"})
    save_tasks(username, tasks)
    print("Task added!")

def view_tasks(username):
    tasks = load_tasks(username)
    if not tasks:
        print("No tasks.")
        return
    for task in tasks:
        print(f"{task['id']}: {task['description']} - {task['status']}")

def mark_completed(username):
    tasks = load_tasks(username)
    view_tasks(username)
    task_id = int(input("Enter task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            break
    save_tasks(username, tasks)
    print("Task marked as completed!")

def delete_task(username):
    tasks = load_tasks(username)
    view_tasks(username)
    task_id = int(input("Enter task ID to delete: "))
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(username, tasks)
    print("Task deleted!")


def task_menu(username):
    while True:
        print("\n--- Task Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Logout")
        choice = input("Enter choice: ")
        if choice == '1':
            add_task(username)
        elif choice == '2':
            view_tasks(username)
        elif choice == '3':
            mark_completed(username)
        elif choice == '4':
            delete_task(username)
        elif choice == '5':
            break
        else:
            print("Invalid option.")


def main():
    while True:
        print("\n--- Welcome ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                task_menu(username)
        elif choice == '3':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
