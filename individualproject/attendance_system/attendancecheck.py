from datetime import datetime
attendance_book = {}
def register_name():
    name = input("input your name: ")
    if (check_for_name(name,"attendance_system/register.txt")):
        print("The name already registered!")
        opinion = input("press q for returning to the menu. otherwise, continue: ").strip()
        if opinion == "q":
            menu_switch(print_menu())
        else:
            register_name()
    else:
        file_for_record = open("attendance_system/register.txt","a")
        file_for_record.write(name + "\n")
        file_for_record.close()
        print("recored successfully in the register.txt file")
        opinion = input("do you want to continue adding? press y for yes or exit for no: ").strip()

        while opinion != "y" and opinion != "exit":
            opinion = input("do you want to continue adding? press y for yes or exit for no: ")

        if (opinion == "y"):
            register_name()
        else:
            return

def check_for_name(name,file_path):
    name_file = open(file_path,"r")
    for line in name_file:
        if name == line.strip():
            name_file.close()
            return True
    name_file.close()
    return False

def print_menu():
    print(
"""
________________________

Attendance Record System
________________________
""")
    print("1) register")
    print("2) check-in")
    print("3) check-out")
    print("4) quit")
    option = int(input("choose one from the menu: "))
    if (option <= 4 and option >= 1):
        return option 
    else:
        print("wrong input")
        print_menu()

def check(mode):
    now = datetime.now()
    currTime = now.strftime("%m/%d/%Y, %H:%M:%S")
    name = input("Please enter your name: ")
    if (check_for_name(name,"attendance_system/register.txt")):
        try:
            name_file = open("attendance_system/clients/"+ name +".txt","r")
        
        except FileNotFoundError:
            name_file = open("attendance_system/clients/"+ name +".txt","w")
            name_file.write( currTime + "("+ mode +")\n")
            name_file.close()
            print("new text created")

        else:
            name_file = open("attendance_system/clients/"+ name +".txt","a")
            name_file.write( currTime + "(" + mode + ")\n")
            name_file.close()
            print("text updated in the client directory")
    else:
        print("the input name not registered!")
        print_menu()
        
def menu_switch(option):
    match(option):
        case 1:
            register_name()
        case 2:
            check("in")
        case 3:
            check("out")
        case 4:
            print("System closed.\n")

option = print_menu()
menu_switch(option)