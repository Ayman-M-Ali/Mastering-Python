#-----------------------------------------------------
# Assignment (1) :
#   Create a Function called remove_chars that removes the first and last characters of any String
#   Use map to have this function run over all list items in the assignment
#   Create a variable called cleaned_list and store map results in it
#   Loop the cleaned_list variable to print all the names in the list
#   Use the same example but use the Lambda Function directly inside the Loop
#-----------------------------------------------------

def remove_chars (name) :

  return name[slice(1, -1)]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

for name in map(remove_chars, friends_map) :

  print(name)


# Run Func With Map Into Var
def remove_chars (name) :

  return name[slice(1, -1)]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars, friends_map)

for name in cleaned_list:

  print(name)


# Solution With Lambda Func
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

for name in map(lambda name : name[slice(1, -1)], friends_map) :

  print(name)


print("##### End Assignment (1) #####")

#-----------------------------------------------------
# Assignment (2) :
#   Create a function called get_names that returns names ending with the letter m
#   Use a filter to make this function pass to all list items in the assignment
#   Create a variable called names and store the filter result in it
#   Loop the names variable to print all the names in the list
#   Use the same example but use the Lambda Function directly inside the Loop
#-----------------------------------------------------

def get_names (name) :

  return name.endswith("m")

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names, friends_filter)

for name in names :

  print(name)


# Solution With Lambda Func
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(lambda name : name.endswith("m"), friends_filter)

for name in names :

  print(name)


print("##### End Assignment (2) #####")

#-----------------------------------------------------.
# Assignment (3) :
#   Use what you learned to work out the product of all the numbers in the nums list
#   You should know that a list can change its elements, so the solution must work on any list
#   Do the same solution with Lambda Function
#-----------------------------------------------------

from functools import reduce

def multiplication (num1, num2) :

  return num1 * num2

nums = [2, 4, 6, 2]

result = reduce(multiplication, nums)

result = reduce(lambda num1, num2 : num1 * num2, nums)

print(result)


print("##### End Assignment (3) #####")

#-----------------------------------------------------
# Assignment (4) :
#   Loop the following Tuple with the Index for each element printed
#   Index should start from number 50
#   If you find numbers in the Tuple, ignore it
#   Make sure the data is printed backwards, but not in an organized way
#   Do the solution in two different ways
#-----------------------------------------------------

# Method (1)
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

new_skills = list(reversed(skills))

skills_with_counter = enumerate(new_skills, 50)

for counter, skill in skills_with_counter :

  if type(skill) == int :

    continue

  else:

    print(f'"{counter} - {skill}"')



# Method (2)
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

new_skills = list(reversed(skills))

skills_with_counter = enumerate(new_skills, 50)

skills_top = map(lambda counter, skill : f'{counter} - {skill}', new_skills)

for counter, skill in skills_with_counter :

  if type(skill) == int :

    continue

  else:

    print(f'"{counter} - {skill}"')
