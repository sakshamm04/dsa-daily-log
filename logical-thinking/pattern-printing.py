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
        for k in range(2*(num-i-1) + 1):
            print("* ", end="")
        for l in range(i):
            print("  ", end="")
        print()

# Dual-Side Pyramid pattern
def rhombusPyramidPattern(num):
    for i in range(0, num):
        for j in range(num-i-1):
            print("  ", end="")
        for k in range(2*i+1):
            print("* ",end="")
        for l in range(num-i-1):
            print("  ", end="")
        print()
    for i in range(0, num):
        for j in range(i): 
            print("  ", end="")
        for k in range(2*(num-i-1) + 1):
            print("* ", end="")
        for l in range(i):
            print("  ", end="")
        print()

# Right-Faced Pyramid Pattern
def rightPyramidPattern(num):
    for i in range(2*num-1):
        stars = i+1
        if (i>num-1) :
            stars = 2*num-i-1
        for j in range(stars):
            print("* ",end="")
        print()

# Binary Triangle
def binaryTriangle(num):
    start = 1
    for i in range(num):
        if (i % 2 == 0):
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(f"{start} ",end="")
            start = 1 - start
        print()

# Symmetrical Number Pyramid
def symmetricalNumberPyramid(num):
    for i in range(num):
        for j in range(i+1):
            print(f"{j+1} ", end="")
        for j in range(2*num-2*(i+1)):
            print("  ", end="")
        for j in range(i+1,0, -1):
            print(f"{j} ", end="")
        print()

# Number Triangle Pattern
def numberPyramid(num):
    incrementer = 1
    for i in range(num):
        for j in range(i+1):
            print(f"{incrementer} ", end="")
            incrementer += 1
        print()

# Alphabet Triangle Pattern
def alphabetTriangle(num):
    for i in range(num):
        for j in range(i+1):
            print(f"{chr(65+j)} ", end="")
        print()

# Inverse Alphabet Triangle Pattern 
def inverseAlphabetTriangle(num):
    for i in range(num):
        for j in range(num-i):
            print(f"{chr(65+j)} ", end="")
        print()

# Alphabet Triangle Pattern 2nd Variation 
def alphabetTriangle2(num):
    for i in range(num):
        for j in range(i+1):
            print(f"{chr(65+i)} ", end="")
        print()

# Alphabet Pyramid Pattern
def alphabetPyramidPattern(num):
    for i in range(num):
        for j in range(num-i-1):
            print("  ", end="")

        char_val = 65
        for j in range(2*i+1):
            print(f"{chr(char_val)} ", end="")
            if j<i : char_val+=1
            else: char_val-=1

        for j in range(num-i-1):
            print("  ", end="")
        print()

# Alphabet Triangle Pattern 3rd Variation
def alphabetTriangle3(num):
    for i in range(num):
        char_value = 65 + num - i - 1
        for j in range(i+1):
            print(f"{chr(char_value + j)} ", end="")
        print()

# Hollow Diamond Star Pattern
def hollowStarPattern(num):
    for i in range(num):
        for j in range(num-i):
            print("* ", end="")
        for j in range(2*i):
            print("  ", end="")
        for j in range(num-i):
            print("* ", end="")
        print()
    for i in range(num):
        for j in range(i+1):
            print("* ", end="")
        for j in range(2*(num-i-1)):
            print("  ", end="")
        for j in range(i+1):
            print("* ", end="")
        print()