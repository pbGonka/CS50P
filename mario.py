#mario game ilustration using what we've learned

#height blocks to jump over 

""" 
def main():
    print_column(3)


def print_column(height):
    ''' for _ in range(height):
        print("#")'''
    print("#\n" * height, end="")

main() """

#float blocks that give you coins when you hit them
""" 
def main():
    print_row(4)

def print_row(width):
    print("?" * width)


main()
 """

#a solid 2 dimension square
""" 
def main():
    print_square(3)

def print_square(size):
    #For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        #this empty print is for when you finish to print a line of "bricks" automatically goes to the next line (moving the cursor with it)
        print()

main() """

""" 
def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print("#" * size)

main() """

def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)


main()