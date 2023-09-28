#!/usr/bin/env python
# coding: utf-8

# # Python program for "to do List"

# In[ ]:


tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid index. No task removed.")

def main():
    while True:
        print("\nMenu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            show_tasks()
            index = int(input("Enter the index of the task to remove: "))
            remove_task(index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

