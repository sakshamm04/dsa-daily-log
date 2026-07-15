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

# Right-Half Pyramid Number Pattern 2nd Variation
def numberPyramidPattern2(num):
    for i in range(0, num):
        for j in range(0, i+1):
            print(f"{i+1} ", end="")
        print()

# Inverse Right-half Star Pyramid Pattern
def inversePyramidPattern(num):
    for i in range(0, num):
        for j in range(0, num-i):
            print("* ", end="")
        print()

# Inverse Right-half Pyramid Number Pattern
def inversePyramidNumberPattern(num):
    for i in range(0, num):
        for j in range(0, num-i):
            print(f"{j+1} ", end="")
        print()

# Pyramid Pattern
def pyramidPattern(num):
    for i in range(0, num):
        for j in range(num-i-1):
            print("  ", end="")
        for k in range(2*i+1):
            print("* ",end="")
        for l in range(num-i-1):
            print("  ", end="")
        print()

# Inverse Pyramid Pattern
def inversePyramidPattern(num):
    for i in range(0, num):
        for j in range(i): 
            print("  ", end="")
        for k in range(2*num-(2*i+1)):
            print("* ", end="")
        for l in range(i):
            print("  ", end="")
        print()
num = int(input())
inversePyramidPattern(num)