# Digit Concept (Extraction of Digits eg: 7789)
import math

num = int(input())
reversed = 0
count = int(math.log10(num) + 1)
print(count)
while num>0:
    last_digit = num%10
    num = int(num / 10)
    reversed = reversed * 10 + last_digit
print(reversed)