candidates = {
    "White": 0,
    "Red": 0,
    "Blue": 0
}

def view():
    print("The candidates are : ")
    i=1
    for person in candidates:
        print(f"{i}.{person}")
        i+=1
    print("\n")

def vote():
    view()
    choice=input("Vote from given candidates:")
    if choice in candidates:
        candidates[choice]+=1
        print("Thank you.Your vote is recorded.")
    else:
        print("You can vote only from the given candidates")
    print("\n")

def result():
    for person in candidates:
        print(f"{person} : {candidates[person]}")
    print("\n")

def run_voting():

    while True:

        print("1.View candidates")
        print("2.Vote for a candidate")
        print("3.View Result")
        print("4.Exit")
        option=int(input("Choose (1-4) : "))

        if option==1:
            view()
        elif option==2:
            vote()
        elif option==3:
            result()
        elif option==4:
            break
        else:
            print("Invalid option")

print("Welcome to python voting system.")
run_voting()

