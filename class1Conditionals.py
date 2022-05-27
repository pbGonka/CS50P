#Conditionals (if, elif, else)
""" 
x = int(input("What's x? "))
y = int(input("What's y? "))
 """
#1
""" 
if x < y:
    print("x is lower than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
 """
#2
""" if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

 """
#3
""" 
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
 """

#4
""" if x == y:
    print("x is equal to y")
    
else:
    print("x is not equal to y") """

#score = int(input("Score: "))
""" 
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70  and score < 80:
    print("Grade C")
elif score >= 60 and score < 70:
    print("Grade D")
else:
    print("Grade F") """

#2
""" if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
else:
    print("Grade F")
 """

#3
""" if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F") """


#Signs: +, -, *, /, %, **
""" 
x = int(input("What's x? "))

if x % 2 == 0 :
    print("Even number")
else:
    print("Odd number")
 """
""" 
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

main() """

#Cleaner version:
""" def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(number):
    return True if number % 2 == 0 else False

main()
 """
#Even cleaner version:    (since the expression number % 2 == 0 is indeed a boolean expression it will return a boolean answer so you just need to return itself)

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(number):
    return number % 2 == 0

main()

