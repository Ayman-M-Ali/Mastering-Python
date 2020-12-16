#------------------------------------------------------------
# (1)Create a Tuple consisting of one object and be your name without using the brackets () then print the only element in the Tuple on the first line and on the second line print the type to make sure that the type is Tuple
# (2)Create a Tuple containing 3 names of your friends and the first name is Osama
#    Use your experience and what you previously learned to change the first name from Osama to Elzero
#    Print the Tuple content on the first line
#    Print the type to make sure it is a Tuple and not another data type
#    On the third line, print the number of items inside the Tuple
# (3)Create a Tuple containing the numbers 1 through 3
#    Create a Tuple containing the letters A through C.
#    Concatenate them in a new Tuple and print their content on the first line
#    On the second line, Concatenate them in a new Tuple, but take an item from the first, then an item from the second, and so on.
#    On the third line, count the number of items in the new Tuple in the usual way
#    On the fourth line, count the number of items in the new Tuple by a method other than the previous one
# (4)Create a Tuple containing 4 items with any data type you want
#    Destruct the Tuple and Assign the first value for variable a, the second value for variable b, and the fourth value for variable c
#    Print the variable a, b, c each on a different line
#    Make sure you destruct with only one line
#------------------------------------------------------------

# (1)Create a Tuple consisting of one object and be your name without using the brackets () then print the only element in the Tuple on the first line and on the second line print the type to make sure that the type is Tuple
myName = "Ayman",
print(myName)
print(type(myName))

print("#" * 50)

# (2)Create a Tuple containing 3 names of your friends and the first name is Osama
#    Use your experience and what you previously learned to change the first name from Osama to Elzero
#    Print the Tuple content on the first line
#    Print the type to make sure it is a Tuple and not another data type
#    On the third line, print the number of items inside the Tuple
myFriends = ("Osama", "Majd", "Hisham")
guys = list(myFriends)
guys[0] = "Elzero"
print(guys)
print(type(myFriends))
print(len(myFriends))

print("#" * 50)

# (3)Create a Tuple containing the numbers 1 through 3
#    Create a Tuple containing the letters A through C.
#    Concatenate them in a new Tuple and print their content on the first line
#    On the second line, Concatenate them in a new Tuple, but take an item from the first, then an item from the second, and so on.
#    On the third line, count the number of items in the new Tuple in the usual way
#    On the fourth line, count the number of items in the new Tuple by a method other than the previous one
numbers = (1, 2, 3)
letters = ("A", "B", "C")
items = numbers + letters
print(items)
newItems = ((numbers, ) + (letters, ))
print(newItems)
targetTuple = tuple(zip(*newItems))
print(targetTuple)
a, b, c = (targetTuple[0]), (targetTuple[1]), (targetTuple[2])
newSulotion = a + b + c
print(newSulotion)

print(len(items))
print(items.__len__())

print("#" * 50)

# (4)Create a Tuple containing 4 items with any data type you want
#    Destruct the Tuple and Assign the first value for variable a, the second value for variable b, and the fourth value for variable c
#    Print the variable a, b, c each on a different line
#    Make sure you destruct with only one line
media = ("Facebook", "Instegram", "Twitter", "whatsApp")
a, b, _, c = media
print(a)
print(b)
print(c)


