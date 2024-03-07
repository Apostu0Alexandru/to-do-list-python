to_do_list=[]

def add_task(task_test):
    to_do_list.append(task_test)

def display_tasks():
    for i, task in enumerate(to_do_list):
        print(f"{i+1} {task}")

def mark_complete(task_index):
    if 0 <= task_index < len(to_do_list):
        to_do_list[task_index]= "COMPLETED" + to_do_list[task_index]
    else : 
        print ("Invalid task index") 

def remove_task (task_index):
    if 0 <=  task_index < len(to_do_list):
        del to_do_list[task_index]
    else:
        print ("Enter a valid task index")

while True :
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task_text = input("Enter task description: ")
        add_task(task_text)
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        display_tasks()  # Display tasks again for reference
        task_index = int(input("Enter the index of the completed task: ")) - 1
        mark_complete(task_index)
    elif choice == '4':
        display_tasks()  # Display tasks again for reference
        task_index = int(input("Enter the index of the task to remove: ")) - 1
        remove_task(task_index)
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
