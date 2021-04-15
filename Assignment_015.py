#--------------------------------------------------------
# Assignment (1):
#   Write the following code to test yourself and do not run it
#   After the last line in the code write a comment containing the Output that will come out from your point of view
#   Then run Run to see your result sound or not
#   Make a comment before each of the lines in the code to explain how this result appeared
#--------------------------------------------------------

# var => Type of value is Tuple
values = (0, 1, 2)
# if statement : any of values is True:
if any(values):
# Create new var => give value => Zero
  my_var = 0
# Create List That contains True Type  Element
my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
# If All values into List (with Index) Is True :
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
# Give Result "Good"
  print("Good")

else:
# Give Result "Bad"
  print("Bad")

# The result is Good

print("##### End Assignment (1) #####")

#-------------------------------------------------------
# Assignment (2):
#   What is the value of v that causes the print to output the number 820
#-------------------------------------------------------

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

print("##### End Assignment (2) #####")

#-------------------------------------------------------
# Assignment (3):
#   What is the value of the variable n
#-------------------------------------------------------

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

print("##### End Assignment (3) #####")

#-------------------------------------------------------
# Assignment (4):
#   Create a function that does the same thing as all and call it my_all
#   Create a function that does the same as any and call it my_any
#   Create a function that does the same as the min and call it my_min
#   Create a function that does the same as the max and call it my_max
#   Make sure my_min + my_max accepts List or Tuple
#-------------------------------------------------------

# func all()
def my_all(nums):

  for n in nums :

    if not n :

      return False

  return True

print(my_all([1, 2, 3]))

print(my_all([1, 2, 3, []]))


# func any()
def my_any(nums):

  for n in nums :

    if n :

      return True

  return False

print(my_any([1, 2, 3]))

print(my_any([0, (), False, []]))


# func min()
def my_min(nums):

  for n in nums :

    if n == min(nums):

      return n

print(my_min([1, 2, 3, -10, -100]))

print(my_min((1, 2, 3, -10, -100)))


# func max()
def my_max(nums) :

  for n in nums :

    if n == max(nums) :

      return n

print(my_max([10, 20, -50, 700]))

print(my_max((10, 20, -50, 700)))
