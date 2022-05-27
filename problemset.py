#Problem set 

#class 0

#1 lowercase an upcase users prompt

""" indoor = input(">>>").lower()

print(indoor)
 """

#2 emulate a playback speed in a frase by using "..." as spaces

""" playback = input(">>>").replace(" ", "...")

print(playback)

 """

 #3 Converting :) or :( to happy or sad emoji faces:

""" 
def main():
    userInput = input()
    print(convert(userInput))

def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

main()
 """

#4 implement a program in Python that prompts the user for mass as an integer (in kilograms) 
#and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
""" 
def main():
    print("Choose a number for mass and I'll give you back the energy from it.")
    mass = int(input("What's the mass? "))
    print("the energy is", einstein(mass))

def einstein(m):
    energy = m*(300000000 **2)
    return int(energy) 
 
main() 
"""
#5 In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. 
# Not to worry, though, we’ve written a tip calculator for you, below!
""" def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main() """
#Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
#dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a
#float. For instance, given $50.00 as input, it should return 50.0.

#percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a
#float. For instance, given 15% as input, it should return 0.15.
""" 
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    d = float(d)
    return round(d)
    


def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p) / 100
    return p


main()
 """


#class 1

#1.  implement a program that prompts the user for the answer to the Great Question of Life, 
#the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
""" 
def main():
    answer = input("What's the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    if great_question(answer) == True:
        print("Yes.")
    else:
        print("No.")

def great_question(answer):
    return answer == "42" or answer == "forty-two" or answer == "forty two"

main()
   """     

#2. implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), 
# output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
""" 
def main():
    greeting = input("Greeting: ").lower()
    answer(greeting)

def answer(greeting):
    if greeting == "hello":
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")

main()
 """

#implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
#gif, .jpg, .jpeg, .png, .pdf, .txt, .zip. If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, 
#which is a common default.
#See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

""" 
def main():
    file_name = input("File name: ").lower()
    file_type(file_name)

def file_type(file_name):
    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main() """

#implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
#x is an integery 
# is +, -, *, or /
# z is an integer 
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

""" 
def main():
    expression = input("Expression: ")
    print(calc(expression))

def calc(result):
    result = result.split()
    x = int(result[0])
    y = result[1]
    z = int(result[2]) 
    if result[1] == "+":
        return float(x + z)
    elif result[1] == "-":
        return float(x - z)
    elif result[1] == "*":
        return float(x * z)
    elif result[1] == "/":
        return float(x / z)
    else:
        print("Sorry, expression not reconized.")

main() """
""" 
def main():
    time = input("What time is it? ")
    if convert(time) >= 7.0 and convert(time) <= 7.59:
        print("Breakfast time")
    elif convert(time) >= 12.0 and convert(time) <= 12.59:
        print("Lunch time")
    elif convert(time) >= 18.0 and convert(time) <= 18.59:
        print("Dinner time")
    

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 100
    return hours + minutes


main()
 """

""" 
def main():
    time = input("What time is it? ")
    if " " in time:
        time, period = time.split(" ")
        convert(time)
    else:
        convert(time)
    if convert(time) >= 7.0 and convert(time) <= 7.59 or convert(time) >= 7.0 and convert(time) <= 7.59 and period == "am":
        print("Breakfast time")
    elif convert(time) >= 12.01 and convert(time) <= 12.59 or convert(time) >= 12.0 and convert(time) <= 12.59 and period == "pm" :
        print("Lunch time")
    elif convert(time) >= 18.0 and convert(time) <= 18.59 or convert(time) >= 6.0 and convert(time) <= 6.59 and period == "pm":
        print("Dinner time")
    

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 100
    return hours + minutes

main() """


#implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.
""" 
camelCase = input("camelCase: ")

#empty variable to store the new snakecased variable
snake_case = ""

#iterate every letter of the input
for i in range(len(camelCase)):
    #now in a camel case one word ends and the other begin when theres an upcase letter, so we search for the upcased letter(s):
    if camelCase[i].isupper():
        #now that the code identified the uper letter, we concatenate the snake_case that is empty with a "_" 
        # and lower the uper letter and continue the iteration and store in snake_case 
        snake_case = snake_case + "_" + camelCase[i].lower()
    else:
        #need to add a case where the theres no uper cased letter:
        #so we just iterate and store in the variable snake_case
        snake_case += camelCase[i]

print("Snake case: ", snake_case)
 """


#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
#implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


""" 
amount = 50
while True:
    if amount > 0:
        print("Amount Due: ", amount)
        coin = int(input("Insert coin: "))
        amount = amount - coin
    elif amount == 0:
        print("Amount Due: ", amount)
        break     
        
    else:
        print("Change owed: ", (amount * -1))
        break
 """

#When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr.
#implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.
""" 
full_input = input("Input: ")
omited_input = ""
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U" ]
for i in range(len(full_input)):
    if full_input[i] in vowels:
        omited_input = omited_input + ""
    else:
         omited_input = omited_input + full_input[i]

print("Output: ", omited_input) """

#In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, 
# with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#Numbers cannot be used in the middle of a plate; they must come at the end. 
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”

#implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
# Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements 
# and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

""" 
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    z = slice(2)
    first_s = s[z]
    y = slice(2,len(s))
    second_s = s[y]

    if len(s) > 6 or len(s) < 2:
        return False
    elif not s.isalnum():
        return False
    elif not first_s.isalpha():
        return False
    elif not second_s.isdecimal():
        return False
    else:
        return True

main() """

#The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … 
# in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the 
# relevant foods in the stores.”
#implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, 
# per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the 
# poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

fruits = {
    "Apple": 130, 
    "Avocado": 50,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Banana": 110,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80,    
}

fruit = input("Fruit: ").capitalize()
if fruit in fruits:
    print("Calories: ", fruits[fruit])
else:
    None