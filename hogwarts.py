### for i in [0, 1, 2]:        a good explanation to iteration and for i in range()
#      print("meow")           for each iteration of the loop i is put at the place of each element of the list and takes the value 
#                              and run the indented line of code with this value * its like i is a variable that varies, asume a value do what the variable needs to do in the 
#                              code and it resets till the loop ends. 


# class about lists using hogwarts as a theme

#students = ["Hermione", "Harry", "Ron", "Draco"]

#lists are made of elements, a group of elements put together, for exemple "hermione" is an element of the list students. Also lista are a type like integers, strings, booleans, etc.
#Every element inside a lista has his own index, it's like the position where the elemento is stored in the list.
#to print out an specific element of a list, I need to specify where the is positioned (indexed). For example if of this list let's say that I want to print out "Harry":
#btw the indexes always starts from 0, the first element of the list is indexed at the position 0. (in the example the element 0 would be "Hermione" the first one of the list)

#print(students[1])

# now let's say I wante to print out every single element of the list. I can use an iteration to run through every single member of the list and print it out, in a loop way.
# I will be calling the elements of the list students as student because it's easier to understand.
""" 
for student in students:
    print(student)
 """

#In here we're iterating the list but by calling the elements by indexes with a variable, in this case called "i", 
""" 
for i in range(len(students)):
    print(students[i])
 """

#Personal proyect: iterate 2 lists and concatenate the indexes of both lists and print it out them. If one of the have more elements the the other, a bigger len(), then
# you need to concatenate "empty" + the element, or element + "empty"
# maybe do a function with an optional argument or a default value???? 
""" 
double = ["Hermione", "Harry", "Ron"]

if len(students) > len(double):
    for i in range(len(students)):
        print(students[i] + " " + "empty")
elif len(double) > len(students):
    for i in range(len(double)):
        print("empty" + " " + double[i])
else:
    for i in range(len(double)):
        print(students[i] + " " + double[i]) """


#What if you want to rank the students in "students = ["Hermione", "Harry", "Ron"]" :
#notice I'm doing i + 1 so it shows as number 1 first instead of 0
""" 
for i in range(len(students)):
    print(i + 1, students[i]) """



# DICTIONARIES dict
""" 
students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin" 
}
 """
#print(students)
#print(students["Hermione"])
#print(students["Draco"])

#only keys
""" 
for student in students:
    print(student) """

#only values
""" 
for student in students:
    print(students[student]) """

#keys + values
""" for student in students:
    print(student, students[student], sep=": ") """

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
""" 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")   
 """
print(students[0])
