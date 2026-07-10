print("=" * 40)
print("        TO-DO LIST MANAGER")
print("=" * 40)

tasks = []

while True:

    print("\nChoose an option:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":

        if len(tasks) == 0:
            print("\nNo tasks available.")

        else:
            print("\nYour Tasks:\n")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":

        task = input("\nEnter new task: ")

        tasks.append(task)

        print("\nTask added successfully!")

    elif choice == "3":

        if len(tasks) == 0:
            print("\nNo tasks to delete.")

        else:
            print("\nYour Tasks:\n")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:

                task_number = int(input("\nEnter task number to delete: "))

                if 1 <= task_number <= len(tasks):

                    removed_task = tasks.pop(task_number - 1)

                    print(f"\n'{removed_task}' deleted successfully!")

                else:
                    print("\nInvalid task number!")

            except ValueError:

                print("\nPlease enter a valid number!")

    elif choice == "4":

        print("\nThank you for using To-Do List Manager!")
        break

    else:

        print("\nInvalid choice! Please try again.")