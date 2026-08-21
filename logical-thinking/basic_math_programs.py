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

    # 4. All divisors
    def divisors(self):
        print("\n")
        print("4. All Divisors")
        # How i did it my own way
        # l = []
        # for i in range(1, self.num +1):
        #     if self.num % i == 0:
        #         l.append(i)
        # print(l)

        # Another Way of doing it
        l = []
        for i in range(1, int(math.sqrt(self.num)) + 1): 
            if int(self.num % i) == 0:
                l.append(i)
                if (int(self.num/i)) != i:
                    l.append(int(self.num/i))
        l.sort() # O(n logn)
        print(l)

    # 5. Prime Number
    def primeNumber(self):
        counter = 0
        for i in range(1, int(math.sqrt(self.num))+1):
            if self.num % i == 0:
                counter += 1
                if int(self.num/i) != i:
                    counter += 1
        if counter == 2:
            print("A prime no.")
        else: 
            print("Not a prime no.")

    # Print all Functions
    def all_programs(self):
        self.extraction_And_Reverse()
        self.check_Palindrome()
        self.armstrong_num()
        self.divisors()
        self.primeNumber()

num = int(input())
obj = Basic_math(num)
obj.all_programs()