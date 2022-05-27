#FUNCTIONS

#going to use the same code used in the begning the "hello.py" :

""" #Ask user for their name

name = input("What's your name? ").strip().title()

#Say hello to user

print(f"hello, {name}")
 """

#using this example we're going to built a function that says "hello" so we don't need to do it every time we want to say that to user.

""" #1 Structuring the algorithm:

#Ask user for their name

name = input("What's your name? ")

#call the function

hello()

#print the return from the input

print(name) 

*if we run the code will be an error because I did not defined the function hello(). Every function that did not come with python, created by the programmer needs to be defined
first with the statement "def" 
"""

""" 
#Define the function we want

def hello():
    print("hello")



#Ask user for their name

name = input("What's your name? ")

#call the function

hello()

#print the return from the input

print(name)

*It will run now, but it's not optimal (run this code to see it.)
"""

""" #Improving the code:

#Define the function we want and putting the parameter (in this case is "to") in the def of the function and also as a second argument in the function print() inside:

def hello(to):
    print("hello,", to)



#Ask user for their name

name = input("What's your name? ")

#call the function, also now we putting the variable name as an argument in the funcion:

hello(name)

 #print the return from the input

#print(name) ****No need to use this anymore, since we are putting the variable name as argument in the hello() function"""

 
""" 
#Improving a little bit more:

#Define the function we want and putting the parameter (in this case is "to") in the def of the function and also as a second argument in the function print() inside:
#also setting a default value for the parameter

def hello(to="world"):
    print("hello,", to)

#Calling the function withou an argumento to see the default value:

hello()

#Ask user for their name

name = input("What's your name? ")

#call the function, also now we putting the variable name as an argument in the funcion:

hello(name)
"""

#SCOPE it´s a term that refers to the location of where a variables value is valid or where it's available for you to use

#I could've used the same name "name" that I've use in the rest of the code as parameter/argument in the function hello() but it was going to be confused to understand as we can see:

""" def hello(name="world"):
    print("hello,", name)

hello()

name = input("What's your name? ")

hello(name) """


#Main function:
#Having the main function at the start of a program makes every other function inside main can be called even before being defined, in other words if I have main, I can
#write the statement to call the function and define later in the code, not like before where you if you call a function before defining it an error occure, like this:

"""Error: 
name = input("What's your name? ")

hello(name)

def hello(to):
    print("hello,", to)
 """


#With main you won't get an error:
""" def main():
    name = input("What's your name? ")
    hello(name)




def hello(to):
    print("hello,", to)

main()
 """


#RETURN

#returns a value from the function (like int(), input(), etc.)
""" 
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    n = n **2
    return n

main()
 """

#Cleaner version, less code lines:

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n **2
    

main()