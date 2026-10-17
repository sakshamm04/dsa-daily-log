# Hashing
num = int(input("Enter a number: "))
arr = []
for i in range(num):
    arrNum = int(input(f"Enter {i+1} number: "))
    arr.append(arrNum)

hashArr = [0] * (max(arr) + 1)
# Pre-Computation
for i in range(len(arr)):
    hashArr[arr[i]] += 1

q = int(input("How many queries you want to enter: "))
for i in range(1, q+1):
    targetNum = int(input(f"Enter target {q}: "))
    print(f"Count of {targetNum}: {hashArr[targetNum]}")