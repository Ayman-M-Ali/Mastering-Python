#-----------------------------------------------------------------
# (1)Make a list that contains the names of your friends and have at least 5 names. In the first and second line is to print the name of the first friend in the list in two ways, then on the third and fourth line you print the name of the last friend in the list in two ways.
# (2)From the previous list print the odd names on the first line and on the second line print the even names.
# (3)Print the group of names No. 2, 3, and 4 in the first line, then the last name and the one before it in the second line, noting that the code should work in case we change the number of items in the list.
# (4)Update the last two names in the list with the name "Elzero"
# (5)Add a name from your friends to the list at the top of the list first, then add another name at the end of the list
# (6)Delete the first two names from the list, then on another line, remove the last name from the list
# (7)Create another two lists with more friends, then add them to the first list to come out with the final list in which all friends
# (8)Arrange the names in the list on the first line from A to Z and in the second line from Z to A
# (9)In the first line, count the number of friends in the first way, and in the second line, count the number of friends in the second way
# (10)Make a list in which the well-known programming languages and within it a submenu with the names of famous frameworks, then in the first line print the name of the first framework in the submenu and in the second line the name of the last framework in the submenu, bearing in mind that the list can increase
#-----------------------------------------------------------------

# Make a list that contains the names of your friends and have at least 5 names. In the first and second line is to print the name of the first friend in the list in two ways, then on the third and fourth line you print the name of the last friend in the list in two ways.
myFriends = ["Osama", "Ahmad", "Salah", "Malek", "Riyad"]
print(myFriends[0])
print(myFriends.pop(0))
print(myFriends[-1])
print(myFriends.pop(-1))

# (2)From the previous list print the odd names on the first line and on the second line print the even names.
print(myFriends[::2])
print(myFriends[1::2])

# (3)Print the group of names No. 2, 3, and 4 in the first line, then the last name and the one before it in the second line, noting that the code should work in case we change the number of items in the list.
print(myFriends[1:4])
print(myFriends[-2:])

# (4)Update the last two names in the list with the name "Elzero"
myFriends[-2:]=["Elzero", "Elzero"]
print(myFriends)

# (5)Add a name from your friends to the list at the top of the list first, then add another name at the end of the list
myFriends.insert(0, "Maher")
print(myFriends)
myFriends.append("Mohammad")
print(myFriends)

# (6)Delete the first two names from the list, then on another line, remove the last name from the list
myFriends = myFriends[2:]
print(myFriends)
myFriends.remove("Mohammad")
# Or This below
myFriends = myFriends[:-1]
print(myFriends)

# (7)Create another two lists with more friends, then add them to the first list to come out with the final list in which all friends
myFriends = ['Ahmad', 'Salah', 'Elzero', 'Elzero']
gym = ["Alaa", "Belal"]
colleages = ["Majd", "Mostafa", "Adnan"]
myFriends.extend(gym)
myFriends.extend(colleages)
print(myFriends)

# (8)Arrange the names in the list on the first line from A to Z and in the second line from Z to A
myFriends.sort()
print(myFriends)
myFriends.sort(reverse=True)
print(myFriends)

# (9)In the first line, count the number of friends in the first way, and in the second line, count the number of friends in the second way
print(len(myFriends))
#Get_List_length = len(myFriends)
#print(Get_List_length)
print (myFriends.__len__())

# (10)Make a list in which the well-known programming languages and within it a submenu with the names of famous frameworks, then in the first line print the name of the first framework in the submenu and in the second line the name of the last framework in the submenu, bearing in mind that the list can increase
programmingLanguages = ["python", "Javascript", "Php", ["Django", "React", "Laravel"]]
print(programmingLanguages[-1][0])
print(programmingLanguages[-1][-1])