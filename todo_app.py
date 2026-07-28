
tasks = []  

#  CREATE 
def add_tasks():
    n = int(input("How many tasks do you want to add? "))

    for i in range(n):
        task = input(f"Enter task {i + 1}: ")
        tasks.append({"task": task, "done": False})

    print("Task(s) added successfully!\n")


#  READ 
def view_tasks():
    if (len(tasks) == 0):
        print("No tasks found.\n")
    else:
        print("\n------ Your Tasks ------")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} [{status}]")
        print()

#  UPDATE 
def update_task():
    if (len(tasks) == 0):
        print("No tasks to update.\n")
        return

    view_tasks()

    index = int(input("Enter task number to update: ")) - 1

    if (0 <= index < len(tasks)):
        new_task = input("Enter the new task: ")
        tasks[index]["task"] = new_task
        print("Task updated successfully!\n")
    else:
        print("Invalid task number.\n")


#  DELETE 
def delete_task():
    if (len(tasks) == 0):
        print("No tasks to delete.\n")
        return

    view_tasks()

    index = int(input("Enter task number to delete: ")) - 1

    if (0 <= index < len(tasks)):
        removed = tasks.pop(index)
        print(f"'{removed['task']}' deleted successfully!\n")
    else:
        print("Invalid task number.\n")



def mark_done():
    if (len(tasks) == 0):
        print("No tasks available.\n")
        return

    view_tasks()

    index = int(input("Enter task number to mark as DONE: ")) - 1

    if (0 <= index < len(tasks)):
        tasks[index]["done"] = True
        print("Task marked as DONE!\n")
    else:
        print("Invalid task number.\n")


# ------------------ MAIN APPLICATION ------------------
while True:

    
    

    print("===== TO-DO APPLICATION =====")
    print("1. Add Task(s)")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as DONE")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_tasks()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        mark_done()

    elif choice == "6":
        print("Thank you for using the To-Do Application!")
        break

    else:
        print("Invalid choice. Please try again.\n")