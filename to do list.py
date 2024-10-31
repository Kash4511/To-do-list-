def list_of_reminders():
    reminders = {}  
    while True:
        add_rem = input("Add a Reminder (or type 'exit' to stop): ")
        if add_rem.lower() == 'exit':
            break
        if add_rem in reminders:
            print(f"\n||{add_rem.capitalize()}||")
            for index, task in enumerate(reminders[add_rem], start=1):
                print(f"{index}. {task}")
            
            edit_choice = input("Do you want to edit the reminder? (yes to edit, no to skip): ").lower()
            if edit_choice == 'yes':
                while True:
                    task_num = input("Enter the task number to mark complete or delete (or type 'back' to go back): ")
                    if task_num.lower() == 'back':
                        break
                    elif task_num.isdigit() and 1 <= int(task_num) <= len(reminders[add_rem]):
                        task_index = int(task_num) - 1
                        action = input("Type 'mc' to mark complete or 'de' to delete: ").lower()
                        
                        if action == 'mc':
                            reminders[add_rem][task_index] += " [Completed]"
                            print(f"Task {task_num} marked as completed.")
                        elif action == 'de':
                            removed_task = reminders[add_rem].pop(task_index)
                            print(f"Task '{removed_task}' deleted.")
                        else:
                            print("Invalid action.")
                    else:
                        print("Invalid task number.")
        else:
            reminders[add_rem] = []
            while True:
                task = input("Add a task (or type 'done' to finish): ")
                if task.lower() == 'done':
                    break
                reminders[add_rem].append(task)

        print(f"\n||{add_rem.capitalize()}||")
        for index, task in enumerate(reminders[add_rem], start=1):
            print(f"{index}. {task}")
        print("\n")

list_of_reminders()


    
    
