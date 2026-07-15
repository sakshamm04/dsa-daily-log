# Star Square of n*n

def squarePattern(num):
    for i in range(num):
        for j in range(num):
            print("* ",end=" ")
        print()

num = int(input())
squarePattern(num)