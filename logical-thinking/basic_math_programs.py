# Digit Concept (Extraction of Digits eg: 7789)

num = int(input())
reversed = 0
while num>0:
    last_digit = num%10
    num = int(num / 10)
    reversed = reversed * 10 + last_digit
print(reversed)