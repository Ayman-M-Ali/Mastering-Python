#---------------------------------------------------------------
# 1- In the first 4 lines, using the Bool Method print 4 different data types, their result is True
#    On line 5 to 8, using Bool Method print 4 different data types, their result is False
# 2- Create 3 variables with the names of any programming skills you possess and their value is the percentage of your learning of these skills, and they are all above 50%
#    In one line only, and with the Boolean Operators, make sure that your learning rate in all skills is greater than 50%.
#    If Condition should not be used here and the result should be returned True
# 3- Create a variable named num_one and its value is number 10
#    Create a variable called num_two with a value of 20
#    Create a third variable named num whose value is number 20
#    On the first line, print a check result if the variable num is greater than one of the other two variables only and not the two
#    On the second line, print the result of checking if the variable num is greater than the other two variables or not
# 4- Create a variable named num_one and its value is number 10
#    Create a variable called num_two with a value of 20
#    Store the result of adding the two variables into a new variable called result and print it on the first line
#    On the second line find the result of raising the number to Exponent 3
#    On the third line, find the remainder of dividing the number resulting from the previous request by 26000
#    On the fourth line, print the result of dividing the resulting number by 5
#    Make sure the previous number is Float, to know that you have reached the solution correctly
#    On the fifth line, print the type after converting it to String to ensure that it is a String
#---------------------------------------------------------------

#   strat Assignment(1)
#   Bool Method ==> True

print(bool(1))

print(bool(["Apple", 5, (7, 6.1)]))

print(50 > 20)

print(bool("Hi Osama"))

print("="* 10)

#   Bool Method ==> False

print(bool(0))

print(bool([]))

print(bool(None))

print(False)

print("\n####### End Assignment(1) #######\n")

#   strat Assignment(2)
#   Create 3 variables of programming skills > 50%
#   In one line only, with Boolean Operators ==> skills greater than 50%.
#   without using if ==> true
html = 80
css = 60
javascript = 70

print(html and css and javascript > 50)

print("\n####### End Assignment(2) #######\n")

#   start Assignment(3)
#   Create 3 variables num_one, num_two, num = 10, 20, 20
#   check result if num is greater than one of the other two variables only, not two
#   check result if num is greater than the other two variables

num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)

print(num > num_one and num > num_two)

print("\n####### End Assignment(3) #######\n")

# 4- Create 2 variables num_one, num_two = 10, 20
#    Store the result of adding the two variables into a new variable called result and print it on the first line
#    On the second line find the result of raising the number to Exponent 3
#    On the third line, find the remainder of dividing the number resulting from the previous request by 26000
#    On the fourth line, print the result of dividing the resulting number by 5
#    Make sure the previous number is Float, to know that you have reached the solution correctly
#    On the fifth line, print the type after converting it to String to ensure that it is a String

num_one = 10
num_two = 20

result = num_one + num_two # sum two variables
print(result)

print(result ** 3) # exponent 3

new_num = (result ** 3) % 26000 # remainder of divition the number resulting from the previous request by 26000
print(new_num)

division = new_num / 5 # divition by 5
print(division)
print(type(division)) # check result is float number

type_division = str(division)
print(type(type_division)) # convert result to str

# Advanced Method
num_one = 10
num_two = 20

result = num_one + num_two

print(result)

print(result ** 3)

print((result ** 3) % 2600)

print(((result ** 3) % 2600) / 5)

print(type(str(((result ** 3) % 2600) / 5)))
