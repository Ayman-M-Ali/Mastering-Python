#----------------------------------------------------------------
#Assinment_010
# No (1)
#Create a variable called num which is an input that accepts a specific number from the person
#Make sure that the number is int and is greater than 0, and if it is not greater than 0, print a message stating this
#After entering the number, print the smaller number directly, the smaller number then the smallest until you reach the number 1
#The number itself should not be printed and the number 0 not printed
#If the numbers contain the number 6, do not print it among the numbers
#After the numbers are printed, print a message stating that all the numbers have been successfully printed and write how many numbers have been printed

num = int(input("Input Your Number: "))

index = 0

if type(num) == int and num > 0:

  while num > 0:

   num -= 1

   if num in (0, 6):

      continue

   print(num)

   index += 1

  else:

   print(f"{index} Numbers Printed Successfully.")

else:

  print(f"Number {num} Is Not Larger Than 0")

print("\n##### End Of Assignment 1 #####\n")

#-----------------------------------------------------------------
# No (2)
#Create a list with five of your friends, then make sure that they have at least two names written in small letters and the rest is the first letter of the name Capital
#Use While Loop to print all the names ignoring the names starting in lowercase letters
#Print the number of names that are ignored and it should be in a programmatic way, not manually

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

ignored = 0

while friends:

	if friends[0][0].islower():

		friends.pop(0)

		ignored += 1

	else:
  		print(friends.pop(0))

else:
	print(f"Friends Printed And Ignored Names Count Is {ignored}")

print("\n##### End Of Assignment 2 #####\n")

#-----------------------------------------------------------------
# No (3)
#Type only one line to print the entire content of the List
#Do not modify anything in the code

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills :
      print(skills.pop(0))
print("\n##### End Of Assignment 3 #####\n")

#------------------------------------------------------------------
# No (4)
#Create an empty list that will later contain your friends' names and put it in a variable called my_friends
#Set the maximum number of friends to add to the list is 4
#Create an Input asks for the name of the person you want to add to the list
#If the person's full name is in uppercase, reject the person and show a message stating that the name is invalid
#If the name is all lowercase, convert the first letter only to an uppercase letter and then add it to the list
#After adding the name, a message will be printed with it stating that you have converted the first letter into a capital letter
#The name of the person must be printed with the letter of addition
#If the person has written a name and the first letter in it is capitalized, add it directly and type a message stating the addition
#In the event that the name has been added and there is still another place in the list, show the Input to add another name until the list is filled
#With each addition, write a message stating how many names are left in the list before it becomes full
#Each name that is added must remove the spaces before and after it, if any
#-----------------------------------------------------------------

my_friends = []

max_friends = 4

while 0 < max_friends:

  friend_input = input("Write Friend Name > ").strip()

  if friend_input.isupper():

   print("Invalid Name")

  else:

   if friend_input.islower():

      print(f"Friend {friend_input} Added => 1st Letter Become Capital")

      friend_input = friend_input.title()

   else:

      print(f"Friend {friend_input} Added")

   my_friends.append(friend_input)

   max_friends -= 1

   print(f"{max_friends} Friends Left.")

else:

  print("Friend List Is Full")