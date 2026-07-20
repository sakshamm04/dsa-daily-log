class Patterns():

    def __init__(self, num):
        self.num = num

    # 1. Star Square of n*n
    def squarePattern(self):
        print("\n1. Star Square of n*n\n")        
        for i in range(self.num):
            for j in range(self.num):
                print("* ",end="")
            print()

    # 2. Right-Half Pyramid Star Pattern
    def trianglePattern(self):
        print("2. Right-Half Pyramid Star Pattern\n")
        for i in range(self.num):
            for j in range(i+1):
                print("* ",end="")
            print()

    # 3. Right-Half Pyramid Number Pattern
    def numberPyramidPattern(self):
        print("3. Right-Half Pyramid Number Pattern\n")
        for i in range(0, self.num):
            for j in range(0, i+1):
                print(f"{j+1} ", end="")
            print()

    # 4. Right-Half Pyramid Number Pattern 2nd Variation
    def numberPyramidPattern2(self):
        print("4. Right-Half Pyramid Number Pattern 2nd Variation\n")
        for i in range(0, self.num):
            for j in range(0, i+1):
                print(f"{i+1} ", end="")
            print()

    # 5. Inverse Right-half Star Pyramid Pattern
    def inverseTrianglePattern(self):
        print("5. Inverse Right-half Star Pyramid Pattern\n")
        for i in range(0, self.num):
            for j in range(0, self.num-i):
                print("* ", end="")
            print()

    # 6. Inverse Right-half Pyramid Number Pattern
    def inversePyramidNumberPattern(self):
        print("6. Inverse Right-half Pyramid Number Pattern\n")
        for i in range(0, self.num):
            for j in range(0, self.num-i):
                print(f"{j+1} ", end="")
            print()

    # 7. Pyramid Pattern
    def pyramidPattern(self):
        print("7. Pyramid Pattern\n")
        for i in range(0, self.num):
            for j in range(self.num-i-1):
                print("  ", end="")
            for k in range(2*i+1):
                print("* ",end="")
            for l in range(self.num-i-1):
                print("  ", end="")
            print()

    # 8. Inverse Pyramid Pattern
    def inversePyramidPattern(self):
        print("8. Inverse Pyramid Pattern\n")
        for i in range(0, self.num):
            for j in range(i): 
                print("  ", end="")
            for k in range(2*(self.num-i-1) + 1):
                print("* ", end="")
            for l in range(i):
                print("  ", end="")
            print()

    # 9. Dual-Side Pyramid pattern
    def rhombusPyramidPattern(self):
        print("9. Dual-Side Pyramid pattern\n")
        for i in range(0, self.num):
            for j in range(self.num-i-1):
                print("  ", end="")
            for k in range(2*i+1):
                print("* ",end="")
            for l in range(self.num-i-1):
                print("  ", end="")
            print()
        for i in range(0, self.num):
            for j in range(i): 
                print("  ", end="")
            for k in range(2*(self.num-i-1) + 1):
                print("* ", end="")
            for l in range(i):
                print("  ", end="")
            print()

    # 10. Right-Faced Pyramid Pattern
    def rightPyramidPattern(self):
        print("10. Right-Faced Pyramid Pattern\n")
        for i in range(2*self.num-1):
            stars = i+1
            if (i>self.num-1) :
                stars = 2*self.num-i-1
            for j in range(stars):
                print("* ",end="")
            print()

    # 11. Binary Triangle
    def binaryTriangle(self):
        print("11. Binary Triangle\n")
        start = 1
        for i in range(self.num):
            if (i % 2 == 0):
                start = 1
            else:
                start = 0
            for j in range(i+1):
                print(f"{start} ",end="")
                start = 1 - start
            print()

    # 12. Symmetrical Number Pyramid
    def symmetricalNumberPyramid(self):
        print("12. Symmetrical Number Pyramid\n")
        for i in range(self.num):
            for j in range(i+1):
                print(f"{j+1} ", end="")
            for j in range(2*self.num-2*(i+1)):
                print("  ", end="")
            for j in range(i+1,0, -1):
                print(f"{j} ", end="")
            print()

    # 13. Number Triangle Pattern
    def numberPyramid(self):
        print("13. Number Triangle Pattern\n")
        incrementer = 1
        for i in range(self.num):
            for j in range(i+1):
                print(f"{incrementer} ", end="")
                incrementer += 1
            print()

    # 14. Alphabet Triangle Pattern
    def alphabetTriangle(self):
        print("14. Alphabet Triangle Pattern\n")
        for i in range(self.num):
            for j in range(i+1):
                print(f"{chr(65+j)} ", end="")
            print()

    # 15. Inverse Alphabet Triangle Pattern 
    def inverseAlphabetTriangle(self):
        print("15. Inverse Alphabet Triangle Pattern\n")
        for i in range(self.num):
            for j in range(self.num-i):
                print(f"{chr(65+j)} ", end="")
            print()

    # 16. Alphabet Triangle Pattern 2nd Variation 
    def alphabetTriangle2(self):
        print("16. Alphabet Triangle Pattern 2nd Variation\n")
        for i in range(self.num):
            for j in range(i+1):
                print(f"{chr(65+i)} ", end="")
            print()

    # 17. Alphabet Pyramid Pattern
    def alphabetPyramidPattern(self):
        print("17. Alphabet Pyramid Pattern\n")
        for i in range(self.num):
            for j in range(self.num-i-1):
                print("  ", end="")

            char_val = 65
            for j in range(2*i+1):
                print(f"{chr(char_val)} ", end="")
                if j<i : char_val+=1
                else: char_val-=1

            for j in range(self.num-i-1):
                print("  ", end="")
            print()

    # 18. Alphabet Triangle Pattern 3rd Variation
    def alphabetTriangle3(self):
        print("# 18. Alphabet Triangle Pattern 3rd Variation\n")
        char_val = 69
        for i in range(self.num):
            for j in range(i+1):
                print(f"{chr(char_val + j)} ", end="")
            print()
            char_val -= 1

    # 19. Hollow Diamond Star Pattern
    def hollowStarPattern(self):
        print("# 19. Hollow Diamond Star Pattern\n")
        for i in range(self.num):
            for j in range(self.num-i):
                print("* ", end="")
            for j in range(2*i):
                print("  ", end="")
            for j in range(self.num-i):
                print("* ", end="")
            print()
        for i in range(self.num):
            for j in range(i+1):
                print("* ", end="")
            for j in range(2*(self.num-i-1)):
                print("  ", end="")
            for j in range(i+1):
                print("* ", end="")
            print()

    # 20. Butterfly Star Pattern
    def butterflyStarPattern(self):
        print("# 20. Butterfly Star Pattern\n")
        
        # THIS IS 1st WAY THAT CAME TO MY MIND IN ORDER TO SOLVE THIS

        # for i in range(self.num):
        #     for j in range(i+1):
        #         print("* ", end="")
        #     for j in range(2*(self.num-i-1)):
        #         print("  ", end="")
        #     for j in range(i+1):
        #         print("* ", end="")
        #     print()
        # for i in range(self.num-1):
        #     for j in range(self.num-i-1):
        #         print("* ", end="")
        #     for j in range(2*(i+1)):
        #         print("  ", end="")
        #     for j in range(self.num-i-1):
        #         print("* ", end="")
        #     print()

        # 2nd WAY OF DOING IT

        for i in range(2*self.num-1):
            stars = i+1
            spaces = 2*(self.num-i-1)
            if i>self.num-1:
                stars = 2*self.num-i-1
                spaces = 2*(i+1)- 2*self.num
            for j in range(stars):
                print("* ", end="")
            for j in range(spaces):
                print("  ", end="")
            for j in range(stars):
                print("* ", end="")
            print()

    #  21. Hollow Square Pattern
    def hollowSquarePattern(self):
        print("21. Hollow Square Pattern\n")
        for i in range(self.num):
            for j in range(self.num):
                if i==0 or i==self.num-1 or j==0 or j==self.num-1:
                    print("* ", end="")
                else:
                    print("  ", end="")
            print()

     # 22. Number Square Matrix Pattern
    def numberSquareMatrix(self):
        print("22. Number Square Matrix Pattern\n")
        size = 2*self.num-1
        for i in range(size):
            for j in range(size):
                top = i
                left = j
                bottom = (size-1)-i
                right = (size-1)-j
                min_val = min(top, left, bottom, right)
                print_val = self.num - min_val
                print(f"{print_val} ", end="")
            print()

    def allPatternPrint(self):
        self.squarePattern()
        print("\n")
        self.trianglePattern()
        print("\n")
        self.numberPyramidPattern()
        print("\n")
        self.numberPyramidPattern2()
        print("\n")
        self.inverseTrianglePattern()
        print("\n")
        self.inversePyramidNumberPattern()
        print("\n")
        self.pyramidPattern()
        print("\n")
        self.inversePyramidPattern()
        print("\n")
        self.rhombusPyramidPattern()
        print("\n")
        self.rightPyramidPattern()
        print("\n")
        self.binaryTriangle()
        print("\n")
        self.symmetricalNumberPyramid()
        print("\n")
        self.numberPyramid()
        print("\n")
        self.alphabetTriangle()
        print("\n")
        self.inverseAlphabetTriangle()
        print("\n")
        self.alphabetTriangle2()
        print("\n")
        self.alphabetPyramidPattern()
        print("\n")
        self.alphabetTriangle3()
        print("\n")
        self.hollowStarPattern()
        print("\n")
        self.butterflyStarPattern()
        print("\n")
        self.hollowSquarePattern()
        print("\n")
        self.numberSquareMatrix()

while True:
    num = input("Enter a Number: ")
    if not num.isdigit() or int(num) == 0 :
        print("Print a valid positive number next time!")
    else:
        num = int(num)
        break

p = Patterns(num)
p.allPatternPrint()