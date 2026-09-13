class recursion:

    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        elif num < 0:
            return "Factorial of -ve numbers is not possible!"
        else:
            return num * self.factorial(num-1)


    def fibonacci(self, num):
        # # Brute Force
        # l = []
        # n = 0
        # for i in range(num+1):
        #     if i == 0 or i == 1:
        #         l.append(i)
        #         continue
        #     else:
        #         n = l[i-1] + l[i-2]
        #         l.append(n)
        # print(l)

        # Better Approach
        if num <= 1:
            return num
        return self.fibonacci(num-1) + self.fibonacci(num-2)
        


    def sumFirstN(self, num):
        if num == 0:
            return 0
        elif num < 0:
            print("Enter a number bigger than 0!")
        else: 
            return num + self.sumFirstN(num-1)


    def reverseArr(self, l, i): # def reverseArr(l, l_c):
    #     # Brute Force (T.C = O(n))
    #     # n = len(l)
    #     # for i in range(n):
    #     #     l_c.append(l[n-i-1])

        # Optimal Approach (T.C = O(n/2))
        n = len(l)
        if i >= n // 2:
            return
        l[i], l[n - i - 1] = l[n - i - 1], l[i]
        self.reverseArr(l, i + 1)


    def stringPalindrome(self, s, i): # def stringPalindrome(string):
        # # Brute Force :
        # n = len(string)
        # s = ""
        # for i in range(n):
        #     s += string[n-i-1]
        # print(s)
        # if string == s:
        #     print("Palindrome!")
        # else:
        #     print("Not Palindrome")

        # Optimal Approach :
        n = len(s)
        if i >= n // 2:
            return True
        if s[i] != s[n-i-1]:
            return False
        return self.stringPalindrome(s, i+1)

r = recursion()