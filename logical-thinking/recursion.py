# class recursion:
#     def __init__(self):
#         pass

def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return "Factorial of -ve numbers is not possible!"
    else:
        return num * factorial(num-1)

def sumFirstN(num):
    if num == 0:
        return 0
    elif num < 0:
        print("Enter a number bigger than 0!")
    else: 
        return num + sumFirstN(num-1)

def reverseArr(p, q):
    if(p >= q):
        return
    reverseArr(p+1, q-1)
 