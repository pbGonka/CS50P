#calculator

# With integers

#1
""" x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z) """

#2
""" x = input("What's x? ")
y = input("What's y? ")

print(int(x) + int(y)) """

#3
""" x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y) """

#4

""" print("Result:", (int(input("first number?: ")) + int(input("second number?: ")))) """

#With float

#Ask the user and convert the return value from the input to float
""" x = float(input("What's x? "))
y = float(input("What's y? ")) """

#Execute the sum of the variables, round them up to closest integer, and print it out the answer
#z = round(x + y)

#print(z)

#You can use round() function to round up the number to the closest integer. round(number[, ndigits])

#format big numbers to make them more readable 
#(the use of "," and "." it depends on the country and how they use, in the US they use "," to separate the 0 on thousands, millions, etc. and on things like cents, they use the ".")

#print(f"{z:,}")  

#rounding the division and choosing how many decimals after the "," (using a division)

""" x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z) """

#other way to solve the code above:

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y 

#other way to round up the float result of the division in the print statement is by using the format (f) with the other cyptic that python has (the .2f). * The 2 in the ".2f" it's the number of decimals after the floating point
print(f"{z:.2f}")


