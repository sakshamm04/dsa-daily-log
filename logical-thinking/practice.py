import math

# Digit Extraction:
def digit_Extraction(num):
    reversed = 0
    while(num>0):
        last_digit = num%10
        reversed = reversed * 10 + last_digit
        num = int(num / 10)
    print(reversed)

def armstrong(num):
    numCopy = num
    sumNum = 0
    while numCopy>0 :
        last_digit = numCopy % 10
        sumNum = sumNum + (last_digit**3)
        numCopy = int(numCopy / 10)
    if num == sumNum :
        print("True")
    else :
        print("False")

def all_divisors(num):
    l = []
    for i in range(1, int(math.sqrt(num) + 1)) :
        if int(num % i) == 0 :
            l.append(i)
            if (int(num/i)) != i :
                l.append(int(num/i))
    l.sort()
    print(l)
num = int(input())
all_divisors(num)
