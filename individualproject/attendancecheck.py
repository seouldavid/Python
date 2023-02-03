def register_name():
    name = input("input your name: ")
    if (check_for_name(name,"individualproject/register.txt")):
        print("The name already registered!")
        #wish to ask whether to continue adding or not
        opinion = input("press q for returning to the menu. otherwise, continue: ").strip()
        if opinion == "q":
            return
        else:
            register_name()
    else:
        file_for_record = open("individualproject/register.txt","a")
        file_for_record.write(name + "\n")
        file_for_record.close()
        print("recored successfully")
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
        
register_name()