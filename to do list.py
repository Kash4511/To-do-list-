def list_of_reminders():
    reminders = {}  
    while True:
        add_rem = input("Add a Reminder (or type exit to stop): ")
        if add_rem.lower() == 'exit':
            break
        if add_rem in reminders:
            print("the list of reminders already exists.")
            break
        else:
            reminders[add_rem] =[]
            while True:
                task = input("Add a task: ")
                if task == 'done':
                    break
                reminders[add_rem].append(task)
        print(f"\n||{add_rem.capitalize()}||")
        for index, task in enumerate(reminders[add_rem], start =1):
            print(f"{index}. {task.capitalize()}")
        print("\n")
        

            
list_of_reminders()

    
    
