# from datetime import datetime
# attendance_book = {}
# # retrieve name
# name = input("Enter your name: (for exit, press q)")
# while (name != "q"):
#     now = datetime.now()
#     currTime = now.strftime("%m/%d/%Y, %H:%M:%S")
#     if name in attendance_book:
#         if (attendance_book[name][-1][attendance_book[name][-1].find("(")+1:attendance_book[name][-1].find(")")] == "in"):
#             attendance_book[name].append(" " + currTime + "(out)")
#         else:
#             attendance_book[name].append(" " + currTime + "(in)")

#         print(attendance_book)
#     else:
#         attendance_book[name] = []
#         attendance_book[name].append(currTime + "(in)")
#         print(attendance_book)
#     name = input("Enter your name: (for exit, press q)")
# print("\nExit\n")

#pop up menu 1.record in,out 2.ask personal info 3.register
# record calls text from outside and personal info reads from file
# register writes or updates file
# when calling 1,2 if the name is not in file, error prompts then say the inptted
# user is not registered then ask whether want to register. If yes go to the register menu
def register_name():
    name = input("input your name: ")
    if (check_for_name(name,"individualproject/register.txt")):
        print("The name already registered!")
        register_name()
    else:
        file_for_record = open("individualproject/register.txt","a")
        file_for_record.write(name + "\n")
        file_for_record.close()
        print("recored successfully")
        opinion = input("do you want to continue adding? press exit if no")
        

def check_for_name(name,file_path):
    name_file = open(file_path,"r")
    for line in name_file:
        if name == line.strip():
            name_file.close()
            return True
    name_file.close()
    return False
        
