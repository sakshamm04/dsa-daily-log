# Star Square of n*n
def squarePattern(num):
    for i in range(num):
        for j in range(num):
            print("* ",end=" ")
        print()

# Triangle Star Pattern
def trianglePattern(num):
    for i in range(num):
        for j in range(i+1):
            print("* ",end=" ")
        print()

