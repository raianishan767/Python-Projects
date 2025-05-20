print("Welcome to our to do list")

try:
    with open("tasks.txt","r") as file:
        tasks=file.read().splitlines()
except FileNotFoundError:
    tasks=[]

while True:
    print("1.View Text")
    print("2.Add Text")
    print("3.Remove Text")
    print("4.Exit")

    option=int(input("Enter your choice : "))

    if option==1:
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your Tasks :\n")
            i=1
            for task in tasks:
                print(f"{i}.{task}")
                i+=1

    elif option==2:
        task=input("Enter task : ")
        tasks.append(task)
        with open("tasks.txt","w") as file:
            for i in tasks:
                file.write(i+"\n")
            print("Task is added")

    elif option==3:
        if not tasks:
            print("No task is available to remove.")
        else:
          i=1
          for task in tasks:
            print(f"{i}.{task}")
            i+=1
          try:
            num=int(input("Enter the task number to be removed : "))
            removed=tasks.pop(num-1)
            with open("tasks.txt","w") as file:
             for i in tasks:
                file.write(i+"\n")
             print("Task is removed.")
          except:
              print("Invalid number")
    elif option==4:
        print("Good bye.") 
    else:
        print("Enter a valid number.")
