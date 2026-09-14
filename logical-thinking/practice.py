# import math

# # Digit Extraction:
# def digit_Extraction(num):
#     reversed = 0
#     while(num>0):
#         last_digit = num%10
#         reversed = reversed * 10 + last_digit
#         num = int(num / 10)
#     print(reversed)

# def armstrong(num):
#     numCopy = num
#     sumNum = 0
#     while numCopy>0 :
#         last_digit = numCopy % 10
#         sumNum = sumNum + (last_digit**3)
#         numCopy = int(numCopy / 10)
#     if num == sumNum :
#         print("True")
#     else :
#         print("False")

# def all_divisors(num):
#     l = []
#     for i in range(1, int(math.sqrt(num) + 1)) :
#         if int(num % i) == 0 :
#             l.append(i)
#             if (int(num/i)) != i :
#                 l.append(int(num/i))
#     l.sort()
#     print(l)

# def grade(num1, num2, num3):
#     total = num1 + num2 + num3
#     percentage = round((((num1+num2+num3)*100)/300), 2)
#     print(f"Total: {total}\nPercentage: {percentage}")
#     if percentage < 40:
#         print("Grade F")
#     elif percentage < 60:
#         print("Grade C")
#     elif percentage < 80:
#         print("Grade B")
#     elif percentage < 90:
#         print("Grade A")
#     elif percentage < 100:
#         print("Grade S")
#     else:
#         print("Invalid!")

# def alphabetTriangle(num):
#     for i in range(num):
#         for j in range(num-i-1):
#             print("  ", end="")

#         char = 65
#         for j in range(2*i+1):
#             print(f"{chr(char)} ", end="")
#             if j<i : char+=1
#             else : char-=1

#         for j in range(num-i-1):
#             print("  ", end="")

#         print()

# def alphabetPyramid(num):
#     for i in range(5):
#         var = 65
#         for j in range((num-i-1)):
#             print("  ",end="")
#         for j in range((2*i)+1):
#             print(f"{chr(var)}",end=" ")
#             if i>j: var+=1
#             else: var-=1
#         for j in range((num-i-1)):
#             print("  ",end="")
#         print()


def numberSquare(num):
    for i in range((2*num)-1):
        size = 2*num-1
        for j in range((2*num)-1):
            top = i
            bottom = (size-1)-i
            left = j
            right = (size-1)-j
            mini = min(top, bottom, left, right)
            layer = num - mini
            print(layer, end=" ")
        print()