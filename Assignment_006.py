#--------------------------------------------------------------------
# (1)Create a list containing the following numbers 1, 2, 3, 3, 4, 5, 1
#    Create a variable named unique_list and store only the values unique from the previous list.
#    On the first line print the unique_list content and make sure it contains only the special numbers
#    On the second line print the unique_list type and make sure the data type is list
#    On the third line, print the unique_list without the last element
# (2)Create a New Set containing the numbers 1, 2, 3
#    Create a New Set containing the letters A, B, and C.
#    Merge the first and second sets into a new one
#    Merge the first and second sets into a new one in a second way
#    Merge the first and second sets into a new one in a third way
#    Merge the first and second sets into a new one in a fourth way
#    Print all of the previous sets on the 4 lines
# (3)Create a Set containing items 1, 2, 3
#    On the first line, print the set content
#    Empty the entire set content with only one line, then print the content on the second line to make sure it is completely blank
#    Add two “A” and “B” elements to this set and print their content on the third line
#    Try to remove the "C" element, of course, the element does not exist. Make sure that you will not get an error when you try to remove the non-existing element
# (4)Create a Set containing items 1, 2, 3
#    Create a Second Set containing 1, 2, 3, 4, 5, 6
#    Make sure that all the contents of the first set are present in the second or not
# (5)Create a dictionary containing four programming skills with the percentage of your level in them in them
#    Without Looping, print each skill on a line with the percentage written level next to it
#    Add a new skill to the Dictionary with its percentage and then print it on the fifth line
#--------------------------------------------------------------------

# (1)Create a list containing the following numbers 1, 2, 3, 3, 4, 5, 1
#    Create a variable named unique_list and store only the values unique from the previous list.
#    On the first line print the unique_list content and make sure it contains only the unique numbers
#    On the second line print the unique_list type and make sure the data type is list
#    On the third line, print the unique_list without the last element
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[:4])

print("=" *50)
#=========================================================================
# (2)Create a New Set containing the numbers 1, 2, 3
#    Create a New Set containing the letters A, B, and C.
#    Merge the first and second sets into a new one
#    Merge the first and second sets into a new one in a second way
#    Merge the first and second sets into a new one in a third way
#    Merge the first and second sets into a new one in a fourth way
#    Print all of the previous sets on the 4 line
nums = {1, 2, 3}
letters = {"A", "B", "C"}
nums | letters
nums.union(letters)
nums.update(letters)
for i in nums:
    print((i) + ',' + (letters))
#import operator
#from functools import reduce
#reduce(operator.or_, [nums, letters])
print(nums)
print(nums)
print(nums)



print("=" *50)
#=========================================================================
# (3)Create a Set containing items 1, 2, 3
#    On the first line, print the set content
#    Empty the entire set content with only one line, then print the content on the second line to make sure it is completely blank
#    Add two “A” and “B” elements to this set and print their content on the third line
#    Try to remove the "C" element, of course, the element does not exist. Make sure that you will not get an error when you try to remove the non-existing element
items = {1, 2, 3}
print(items)
items.clear()
print(items)
newSet = {"A", "B"}
items.update(newSet)
print(items)
print(items.discard("C"))

print("=" *50)
#=========================================================================
# (4)Create a Set containing items 1, 2, 3
#    Create a Second Set containing 1, 2, 3, 4, 5, 6
#    Make sure that all the contents of the first set are present in the second or not
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))

print("=" *50)
#=========================================================================
# (5)Create a dictionary containing four programming skills with the percentage of your level in them
#    Without Looping, print each skill on a line with the percentage written level next to it
#    Add a new skill to the Dictionary with its percentage and then print it on the fifth line

my_dict = {
    "HTML" : "90%",
    "Css" : "90%",
    "Js" : "90%",
    "Python" : "90%"
}
my_dict.update({"API" : "20%"})
print(f"'{'HTML'} progress Is {my_dict.get('HTML')}'")
print(f"'{'Css'} progress Is {my_dict.get('Css')}'")
print(f"'{'Js'} progress Is {my_dict.get('Js')}'")
print(f"'{'Python'} progress Is {my_dict.get('Python')}'")
print(f"'{'API'} progress Is {my_dict.get('API')}'")
