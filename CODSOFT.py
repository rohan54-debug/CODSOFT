tasks = []

def add_task():
    task_name = input("Enter a new task: ")
    task = {"task": task_name, "status": "Pending"}
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]['task']} - {tasks[i]['status']}")

def update_task():
    view_tasks()
    if len(tasks) == 0:
        return
    
    try:
        num = int(input("Enter task number to update: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return
        
        new_task = input("Enter new task name: ")
        tasks[num-1]["task"] = new_task
        print("Task updated.")
    except:
        print("Please enter a valid number.")

def complete_task():
    view_tasks()
    if len(tasks) == 0:
        return

    try:
        num = int(input("Enter task number to mark completed: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return
        
        tasks[num-1]["status"] = "Completed"
        print("Task marked as completed.")
    except:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return

    try:
        num = int(input("Enter task number to delete: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return
        
        tasks.pop(num-1)
        print("Task deleted.")
    except:
        print("Please enter a valid number.")

while True:
    print("\n---------- TO DO LIST ----------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Program closed.")
        break
    else:
        print("Wrong choice. Try again.")
