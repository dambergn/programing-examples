def option1():
    print("***option1")
    menu()

def option2():
    print("***option2")
    menu()

def option3():
    print("***option3")
    menu()

def option4():
    print("***option4")
    menu()

def exitprog():
    input("Exiting Program, hit enter to exit program")
    exit()

def menu():
    print("menu")
    print("option 1 | option 2 | option 3")
    print("option 4 |          | exit")
    choice = None
    question = "Choice: "
    choice = input(question)
    match choice.lower().replace(" ", ""):
        case 'option1':
            option1()
        case 'option2':
            option2()
        case 'option3':
            option3()
        case 'option4':
            option4()
        case 'exit':
            exitprog()
        case 'quit':
            exitprog()
        case _:
            print("Not a valid option, please select an option on the menu")
            menu()
 
menu()