# Star Square of n*n
def squarePattern(num):
    for i in range(num):
        for j in range(num):
            print("* ",end=" ")
        print()

# Right-Half Pyramid Star Pattern
def trianglePattern(num):
    for i in range(num):
        for j in range(i+1):
            print("* ",end=" ")
        print()

# Right-Half Pyramid Number Pattern
def numberPyramidPattern(num):
    for i in range(0, num):
        for j in range(0, i+1):
            print(f"{j+1} ", end="")
        print()
