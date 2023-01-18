from datetime import datetime

now = datetime.now()
attendanceBook = {}
# retrieve name
name = input("Enter your name: (for exit, press q)")
while (name != "q"):
    currTime = now.strftime("%m/%d/%Y, %H:%M:%S")
    if name in attendanceBook:
        attendanceBook[name] += " " + currTime + "(out)"
        print(attendanceBook)
    else:
        attendanceBook[name] = currTime + "(in)"
        print(attendanceBook)
    name = input("Enter your name: (for exit, press q)")
print("\nExit\n")