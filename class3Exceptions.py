#Exceptions

#print("hello, world) syntax erro must always be fixed, but sometimes there are some other type of errors like runtime error
#which means that the error occured while the programa is running so its up to you to write some additional code defensively
#to detect the error in case something like that happens. Like for exemple we don't what the user will input and maybe the 
# the input sent by the user gives a traceback or something then you need to be ready and write defensive code to keep the 
# program running 

#x = int(input("What's x? "))  #if the user inputs an string, a traceback error will ocurre, since we cant int() an string (try it) 
#print(f"x is {x}")

#Preventing the error
""" try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer") """

#best practice is to just put the code that you realy think it can give an error, like this
""" try:
    x = int(input("What's x? "))    # like this if the user inputs an string it will give an error, and x won't have a value asigned to it
except ValueError:                  # meaning that x its not defined.    
    print("x is not an integer")

print(f"x is {x}") """
## so to fix it we can use another feature of the try/except, that's the else statement:
""" try:
    x = int(input("What's x? "))    # so what the else does here if it executes the try block, then the else block executes after
except ValueError:                  #but if it goes to the except block it runs what's in the except block and ignores the else block
    print("x is not an integer")    #in other words else only executes if "tried and succeed" above, if not except executes
else:
    print(f"x is {x}") """

#improving the code, so it does not shut it down after the user inputs an string.
""" while True:
    try:
        x = int(input("What's x? "))   #it will loops until we have a valid answer for try and then break out of the loop
    except ValueError:                 #and then run the print function since its out of the loop
        print("x is not an integer")
    else:
        break

print(f"x is {x}") """

#another way (less lines of code):

""" while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}") """

#we can also turn this into a function to use later, since its always common to ask the user for an integer number
""" 
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            int_number = int(input("Number? "))
        except ValueError:
            print("Not a number, please try again.")
        else:
            return int_number         #the return also breaks the loop, so no need to use a break statement

main() """
#implement a more the code, trying to make it wit less lines
""" def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            int_number = int(input("Number? "))
            return int_number
        except ValueError:
            print("Not a number, please try again.") 
        
main()"""

#even less code, since x will receive the return from get_int we can just return the value directly
""" def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("Number? "))
        except ValueError:
            print("Not a number, please try again.")

main() """

#now if you don't want to annoy the user with de message "not a number... Error... etc..." you can just pass the except and then the code will be 
# back to the try block and prompts the user again for a number. Notice that still catchs the error, the error message from the system won't appear   
""" def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("Number? "))
        except ValueError:
            pass

main() """

#change the code, making it more reusable, adding a parameter in get_int() and using it in the caller
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()