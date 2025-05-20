print("Wecome to XYZ contact file.")

contact_file="contacts.txt"
def add_contact():
    name=input("Enter name : ")
    number=input("Enter phone number : ")
    with open(contact_file,"a") as file:
        file.write(f"{name},{number}\n")
    print("Contact is saved")
    print("\n")

def view_contact():
    try:
        with open(contact_file,"r") as file:
            for line in file:
                name,number=line.strip().split(",")
                print(f"{name}-{number}")
    except:
        print("No Contact file.")
    print("\n")
    
def search_contact():
    find=input("Enter name to search : ")
    found=False
    try:
        with open(contact_file,"r") as file:
            for line in file:
                name,number=line.strip().split(",")
                if find.lower()== name.lower():
                    print(f"Number is found : {name}-{number}")
                    found = True
                if not found:
                    print("Number is not added yet.")
    except FileNotFoundError:
        print("File is missing.")
    print("\n")

def contact():
    while True:
        print("1.Add contact")
        print("2.View contact")
        print("3.Search contact")
        print("4.Exit")
        option=int(input("Choose (1-4) : "))
        print("\n")

        if option==1:
            add_contact()
        elif option==2:
            view_contact()
        elif option==3:
            search_contact()
        elif option==4:
            break
        else:
            print("Invalid option.")

contact()

            
    


                

