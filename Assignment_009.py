#------------------------------------------------------------------
#   1-Make two variables called num1, num2 and be Input containing the first and second numbers
#     Create a third variable called operation Input that contains the type of calculation   
#     Make sure that the number variables are Integer and that there are no spaces before or after them
#     Make sure that the variable for the math has no spaces before or after it
#     Get the first and second numbers and the arithmetic operation from the input, then do the operation based on the numbers and the arithmetic operation, whether it is + - * /%
#   2-Make a variable in which the person's age and the value is 17
#     Make a conditional function If Condition on just one line using the Ternary Conditional Operator
#     If the age is over 16, a message appears that the application is suitable for you, and that the application is not suitable for you
#   3-Make an input that accepts the person's age
#     Ensure that the entry is Integer
#     What is required is to print your age in months, weeks, days, hours, minutes, and seconds
#     It is required to print each time unit on a separate line
#     You must make sure that the age is greater than 10 and less than 100, and if not, print a message stating that the age is out of range.
#   4-You have a list of Arab and non-Arab country names
#     You have a discounts value stored in a variable named discount
#     Create an input containing the person's country name and store it in a variable called country
#     Make sure that the name of the country is the first letter with Capital, and there are no spaces before or after it
#     Check if the country is in the country list
#     If it is present, print a letter stating that you have a specific discount and then calculate the discount
#     If it is not in the country, print a letter stating that there are no discounts and print the amount as it is
#     Try entering an existing country once and a non-existent country once to confirm the solution
#-------------------------------------------------------------------

# start Assignment (1)
num1 = input("Add Number One: ").strip()
num2 = input("Add Number Two: ").strip()
operation = input("Add Operation: ").strip()

num1 = int(num1)
num2 = int(num2)

if operation == '+':

    print(num1 + num2)

elif operation == '-':

    print(num1 - num2)

elif operation == '*':

  print(num1 * num2)

elif operation == '/':

    print(num1 / num2)

elif operation == '%':

    print(num1 % num2)

print("\n####### End Assignment (1) #######\n")

#   start Assignment (2)
age = 17

print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You") # if condition

print("\n####### End Assignment (2) #######\n")

#    start Assignment (3)
age_input = input("Input Your Age: ")

age_input = int(age_input)

if 10 < age_input < 100 :                           # if condition

    months = age_input * 12                         # 12 Months Per Year

    weeks = months * 4                              # 4 Weeks Per Month

    days = age_input * 365                          # 365 Days Per Year || months * 30

    hours = days * 24                               # 24 Hours Per Day

    minutes = hours * 60                            # 60 Minutes Per Hour

    seconds = minutes * 60                          # 60 Seconds Per Minute

    print("You Lived for: ")
    print(f'"You Age In Months Are: {months} month."')
    print(f'"You Age In Weeks Are: {weeks} week."')
    print(f'"You Age In Days Are: {days:,} day."')
    print(f'"You Age In Hours Are: {hours:,} hours."')
    print(f'"You Age In Minutes Are: {minutes:,} minutes."')
    print(f'"You Age In Seconds Are: {seconds:,} second."')

else :
    print("Age Is Out of Range")

print("\n####### End Assignment (3) #######\n")

# start Assignment (4)
country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries :


    price -= discount # price = price - discount # 100 - 30 = 70

    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price}")

else:

    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")