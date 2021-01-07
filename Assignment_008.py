#-------------------------------------------------------------------
# 1-Create a variable called name that contains the input for the person’s name
#   Make sure that any spaces before and after the person's name are removed 
#   Make sure the person's name will be the first letter Capital and all other letters Small
#   Print the name along with the welcome message
# 2-Create a variable called age that contains the input for the person's age
#   Make sure the entry will be Integer, not String
#   If the age is younger than 16, print a letter stating that the site contains articles not suitable for the age of under 16
#   If age is 16 or over, print a welcome letter stating the age and that the site is suitable for the person
# 3-Create two variables called first_name and second_name that contain an Input with the person's first and second names
#   Make sure that any spaces before and after the first and second names are removed
#   Make sure that the first and second names are the first letters in them, Capital, and the rest is Small
#   Print a welcome letter containing the first name and the first letter of the second name only.
# 4-Create a variable called email that contains the input of the person's email
#   Make sure to clear the spaces before and after the email
#   Make sure all of the letters are lower letters
#   Print a message on the first line containing only the person's name before the @ sign with the first letter converted to capital
#   Print a message on the second line that only contains the website on which the email is located, without the domain name
#   On the third line, type the Top Level Domain after the "Dot"
#-------------------------------------------------------------------

#   strat Assignment(1)
name = input("Your Name Is: ").strip().capitalize()     # input

print(f"Hello {name}, Nice To Meet You")                # Welcome Message

print("\n####### End Assignment (1) #######\n")

#   strat Assignment(2)
age = int(input('What\'s Your age? ')) # input

if age < 16 :                                           # if condition

    print("the site contains articles not suitable for the age of under 16")

else :

    print("Welcome, the site is suitable for you")

print("\n####### End Assignment (2) #######")

#   start Assignment (3)
first_name = input('What\'s Your First Name? ').strip().capitalize()      # input
second_name = input('What\'s Your Second Name? ').strip().capitalize()    # input 2

print(f"Hello {first_name} {second_name:.1s}.")                           # Welcome Message

print("\n####### End Assignment (2)  ########\n")

#   start Assignment (4)
email = input('What\'s Your Email? ').strip().lower()                             # input

print(f"Your Name Is: " ({email}[ : email.index("@")]).strip().capitalize())                    # userName 

print(email[email.index("@") + 1 : email.index(".")])                     # website 

print(email[email.index(".") + 1 : ])                                     # top Level Domain After Dot
