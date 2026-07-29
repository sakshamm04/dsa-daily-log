import math

class Basic_math:

    def __init__(self, num):
        self.num = num

    # 1. Digit Concept (Extraction of Digits & Reverse)
    def extraction_And_Reverse(self):
        print("\n")
        print("1. Digit Concept (Extraction of Digits & Reverse)")
        numCopy = self.num
        reversed = 0
        count = int(math.log10(numCopy) + 1)
        print(count)
        while numCopy>0:
            last_digit = numCopy%10
            numCopy = int(numCopy / 10)
            reversed = reversed * 10 + last_digit
        print(reversed)

    # 2. Check Palindrome
    def check_Palindrome(self):
        print("\n")
        print("2. Check Palindrome")
        numCopy = self.num
        reversed = 0
        while numCopy>0:
            last_digit = numCopy%10
            numCopy = int(numCopy / 10)
            reversed = reversed * 10 + last_digit
        if reversed == self.num :
            print("True")
        else :
            print("False")

    # 3. Armstrong number
    def armstrong_num(self):
        print("\n")
        print("3. Armstrong Number")
        numCopy = self.num
        sum = 0
        while numCopy>0:
            last_digit = numCopy % 10
            sum = sum + (last_digit**3)
            numCopy = int(numCopy / 10)
        if sum == self.num :
            print("Number is Armstrong")
        else :
            print("Number is not Armstrong")

    def all_programs(self):
        self.extraction_And_Reverse()
        self.check_Palindrome()
        self.armstrong_num()

num = int(input())
obj = Basic_math(num)
obj.all_programs()