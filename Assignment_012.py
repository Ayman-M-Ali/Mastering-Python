#-----------------------------------------------------
# Assignment (1)
# Do a Function that performs calculations called calculate
# The arithmetic operations are addition, subtraction, and division
# The Function contains three Parameters, First Number, Second Number, and the type of calculation and name them as you like
# Do is perform the calculation based on the input
# If the person writes the type of calculation wrong, a message appears for him that there is no such operation
# Available math operations are add, subtract, multiply
# A person can write the math operation in uppercase or lowercase or Mix without a problem. For example add, ADD, aDd
# A person can only write the first letter of the calculation, for example subtract can write S or s
# If the person did not write the mathematical operation at all, do the default operation, which is addition
#-----------------------------------------------------

def calculate (n1, n2, operation) :

  if operation == "add" or operation == "a" or operation == "".strip() :

    print(n1 + n2)

  elif operation == "subtract" or operation == "s" :

    print(n1 - n2)

  elif operation == "multiply" or operation == "m" :

    print(n1 * n2)

  else:

    print("There is no this operation")

calculate(3, 5, "".casefold())

print("##### End Assignment (1) #####")

#-----------------------------------------------------
# Assignment (2)
# Do a Function that performs math operations with the name addition
# The function accepts an unknown number of parameters
# Find the sum of all the numbers passed to the function
# If the number 10 is among the numbers, do not add it to the calculation
# If the number 5 is among the numbers, then subtract it from the rest of the numbers instead of adding them
#-----------------------------------------------------

def addition(*numbers) :

  sum = 0

  for number in numbers :

    if number == 10 or number == 5 :

      continue

    sum += number 

  return sum - 5

print(addition(20, 30, 10, 40, 10, 5))

print("##### End Assignment (2) #####")



#-----------------------------------------------------
# Assignment (3)
# Create a function that prints data about the person and their skills
# The function accepts from you the name of the person and after it an unknown number of skills
# All you have to do is print a welcome letter for the person and then print his / her skills under the name
# If he does not have skills you should show a message stating that he does not have skills yet
#-----------------------------------------------------

def show_skills(name, *skills) :

  if name == "Ayman" :

    print(f"Hello {name} Your Skills is :")

    for skill in skills :

      print(f" - {skill}")

  else :

    print(f"Hello {name} You Have No Skills")

show_skills("Ayman", "Python", "Django")

show_skills("Ahmad", "Python", "Django")

print("##### End Assignment (3) #####")


#-----------------------------------------------------
# Assignment (4)
# Create a function that prints a welcome message for the person
# The function asks you for three parameters: the person's name, age, and country
# If The person did not type any data. Default message appears
#-----------------------------------------------------

def say_hello (name = "Unknown", age = "Unknown", country = "Unknown") :

  print(f"Hello {name} Your Age Is {age} and Your Country Is {country}")

say_hello("Ayman", 37, "Syria")
say_hello()