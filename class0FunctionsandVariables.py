#Ask user for their name

#name = input("What's your name? ")

#Remove whitespaces from string (*does not remove middle empty spaces also lstrip and rstrip) (en el caso de que el usuario aprete sin quere espacios antes o despues de escribir su nombre)
#strip(), capitalize()

#name = name.strip()

#Capitalize user's name (en el caso de que el usuario no ingreso el nombre con la primera letra 
# en mayuscula, y queres que el nombre salga con mayuscula en el programa, pero funcionará solo para el primer nombre)

#name = name.capitalize()

#usando la funcion title todas las primeras letras de las palabras del string serán mayusculas

#name = name.title()

#to clean the code with less lines you can chain the functions

#name = name.strip().title()

#and to have everything even cleaner and compact:

name = input("What's your name? ").strip().title()

#Say hello to user, and put an happy emoji with it (agarré el emoji de emojipedia.org y solo copiar y pegar)

#print("hello,", name, "😀")

#la f (format string) indica a python que es un str especial, como pueden ver tiene la variable entre {}
#y esta encerrado dentro del mismo ""

print(f"hello, {name} 😀")

#mirando el doc de python https://docs.python.org/3/library/functions.html, en la funcion
#print esta definida por: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#asi podemos editar sus *parametros y manipular la funcion para resolver el problema
#de maneras diferentes, como por ejemplo evitar el salto de linea entre 1 print y el otro
#el espacio entre un *argumento y otro.

""" print("hello, ", end='')
print(name, end='')
print(' 😀') """
#print("hello,", name, "😀", sep='???')

#print('"hello, "friend"')
#el \ (backslash)es como un escape
#print("hello, \"friend\"")