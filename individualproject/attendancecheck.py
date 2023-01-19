from datetime import datetime

now = datetime.now()
attendanceBook = {}
# retrieve name
name = input("Enter your name: (for exit, press q)")
while (name != "q"):
    currTime = now.strftime("%m/%d/%Y, %H:%M:%S")
    if name in attendanceBook:
        if (attendanceBook[name][-1][attendanceBook[name][-1].find("(")+1:attendanceBook[name][-1].find(")")] == "in"):
            attendanceBook[name].append(" " + currTime + "(out)")
        else:
            attendanceBook[name].append(" " + currTime + "(in)")

        print(attendanceBook)
    else:
        attendanceBook[name] = []
        attendanceBook[name].append(currTime + "(in)")
        print(attendanceBook)
    name = input("Enter your name: (for exit, press q)")
print("\nExit\n")