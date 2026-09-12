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

def reverseArr(l, i):
    n = len(l)
    if i >= n // 2:
        return
    l[i], l[n - i - 1] = l[n - i - 1], l[i]
    reverseArr(l, i + 1)

l = [1,2,3,4,5]
l_c = l[:]
print(l)
i = 0
reverseArr(l_c, i)
print(l_c)