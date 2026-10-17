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
    def primeNumber(self, n=None):
        if n is None:  # no value passed, fall back to the object's number
            n = self.num
        counter = 0
        for i in range(1, math.isqrt(n) + 1):
            if n % i == 0:
                counter += 1
                if n // i != i:
                    counter += 1
        return 1 if counter == 2 else 0

    # 6. GCD of two numbers 
    # Brute Force, O(min(n1,n2))
    def gcd(self):
        # gcd = 1
        num2 = int(input("Enter an extra num: "))
        # for i in range(min(self.num, num2), 0, -1):
        #     if self.num % i == 0 and num2 % i == 0:
        #         gcd = i
        #         break
        # print(f"GCD = ",gcd)

    # Euclidean Algo, O(log phi (min(a,b)))
        # GCD(a,b) = GCD(a-b,b) OR GCD(a%b,b)
        # Logic: Greater % Smaller (Seperately evauating value of a and b)
        while(self.num > 0 and num2 > 0):
            if self.num > num2:
                self.num = int(self.num % num2)
            else:
                num2 = int(num2 % self.num)
        if self.num == 0:
            print("GCD: ",num2)
        else:
            print("GCD: ",self.num)

    def count_odd(self):
        count = 0
        num_copy = self.num
        while(num_copy > 0):
            last_dig = num_copy % 10
            if last_dig % 2 != 0:
                count += 1
            num_copy //= 10
        print(f"Count of Odd Number: {count}")

    def max_num(self):
        max = 0
        num_copy = self.num
        while(num_copy > 0):
            last_dig = num_copy % 10
            if last_dig > max:
                max = last_dig
            num_copy //= 10
        print(f"Max Number: {max}")

    def perfect_number(self):
        sum_div = 0
        for i in range(1, (self.num // 2) + 1):
            if (self.num % i) == 0:
                sum_div += i
        if sum_div == self.num:
            print("Perfect Number: ",sum_div)
        else:
            print("Not a Perfect Number")

    def all_prime(self):
        count_prime = 0
        i = 2
        while(i <= self.num):
            if self.primeNumber(i):
                count_prime += 1
            i += 1
        print(f"Count of Prime Numbers from {1} to {self.num} = {count_prime}")

    # Print all Functions
    def all_programs(self):
        self.extraction_And_Reverse()
        self.check_Palindrome()
        self.armstrong_num()
        self.divisors()
        self.primeNumber()
        self.gcd()
        self.count_odd()

num = int(input("Enter a number: "))
obj = Basic_math(num)
# obj.all_programs()
obj.count_odd()
obj.max_num()
obj.perfect_number()
obj.all_prime()