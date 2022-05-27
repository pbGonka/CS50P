# Loops
""" 
contador = 0
while contador <= 3:
    print("meow!!")
    contador += 1
     """
""" 
contador = 6
while contador != 0:
    print("meow!")
    contador -= 1 """

""" 
contador = 6
while not contador == 0:
    print("meow!")
    contador -=1 """


""" 
for i in range(6):
    print("meow!") """

"""
names = ["paulo", "daiana", "monti", "jaimico" ]
for name in names:
    print(name)
 """
""" 
names = ["paulo", "daiana", "monti", "jaimico" ]
for i in range(len(names)):
    print(i) """
""" 
for i in range(5):
    print(i)
 """
"""
names = ["paulo", "daiana", "monti", "jaimico" ]
for i in range(len(names)):
    print(names) """

#if you need a variable because it's required by the bif you are using, it's to run this specific code, and that you won't be using later in the programa, you use an "_", it's 
# a good practice to use that. Example:
""" 
for _ in range(3):
    print("meow!")
     """

#funny way to loop:
"""  
print("meow!" * 3)
print("meow!\n" * 3)
print("meow!\n" * 3, end="")
""" 

#to accept only positive number a an input to run the loop till the user inputs a positive number to run the for and "meows"

""" 
while True:
    n = int(input("What's n? "))
    if n > 0:
        break   
 """
#to verify and accept only numbers (and positive). If the user inputs an string it breaks the code when it tries to cast to integer.
""" 
while True:
    n = input("What's n? ")
    if n.isdecimal():
        n = int(n)
        if n > 0:
            break

for _ in range(n):
    print("meow!") """

""" 
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow!")

main() """

""" 
def main():
    number = get_number()
    meow(3)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow!")

main() """

#great example to show how to improve a simple program. Just learned how to do the "cls" in python. Need to import the "os" and use "os.system('cls')". Also learned 
# how to import something inside a function.
#can also see that I've used the return n inside the if statement to break out the loop and hadle the turn to the calling function. 
# I could've used the break and it would be like this:
#...
#   while...
#...    if n > 0:
#       break
#   return n
#...
""" 
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = input("What's n? ")
        if n.isdecimal():
            import os
            os.system('cls')
            n = int(n)
            if n > 0:
                return n

def meow(n):
    for _ in range(n):
        print("meow!")

main()
 """

# LISTS 
### for i in [0, 1, 2]:        a good explanation to iteration and for i in range()
#      print("meow")           for each iteration of the loop i is put at the place of each element of the list and takes the value 
#                              and run the indented line of code with this value * its like i is a variable that varies, asume a value do what the variable needs to do in the 
#                              code and it resets till the loop ends. 

#to see the note that I've made from the class about the lists and dictionaries go to the file hogwarts.py
