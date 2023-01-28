important = open("lessons/ff.txt","r")
read = important.readlines()
for word in read:
    if word[-1] == "\n":
        word = word[:-1]
    print(word, end = " ")