def fib(number):
    if (number == 0):
        return 0
    elif(number <= 3):
        return number
    else:
        return fib(number - 2) + fib(number - 3)
print(fib(8))