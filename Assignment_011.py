#--------------------------------------------------------
# Assignment (1)
#   We have a List of numbers
#   We want to Loop to extract the numbers that are divisible by the number 5 and return an integer
#   We want to automatically print the order of numbers before each number in them
#   We want to print numbers from largest to smallest
#   Print a message stating that the Loop has ended successfully
#--------------------------------------------------------

my_nums = [15, 81, 5, 17, 20, 21, 13]

my_nums.sort(reverse = True)

counter = 1

for num in my_nums :

  if num % 5 == 0 :

    print(f"{counter} => {num}")
    
    counter += 1

print('"All Numbers printed"')

print("###### End Assignment (1) ######")

#--------------------------------------------------------
# Assignment (2)
#   Do a Loop to prints numbers 1 to 20
#   If the number is less than 10, put a zero before it
#   Exclude the numbers 6, 8, and 12
#   Print a message stating that the Loop has ended successfully
#--------------------------------------------------------

my_range = range(1, 21)

for n in my_range :

  if n == 6 or n == 8 or n == 12 :
  
    continue

  print(f"{str(n).zfill(2)}")
  

print('"All Numbers printed successfully"')

print("###### End Assignment (2) ######")


#--------------------------------------------------------
# Assignment (3)
#   You have a dictionary with your scientific material and your rank
#   Each of the values in the Rank has a set of points
#   A is 100, B is 80, and C is 40
#   Use what you learned earlier to get the next result without modifying the original dictionary
#   Print the score at the end after the loop is finished
#--------------------------------------------------------

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

points = {
  "A": 100,
  "B": 80,
  "C": 40
}

total = 0

for rank in my_ranks:

  r = rank  # Rank Name

  v = my_ranks.get(rank)  # Rank Value

  print(f"My Rank in {r} Is {v} And This Equal {points.get(v)} Points")

  total += points.get(v)

else:

  print(f"Total Points Is {total}")

print("\n##### End Of Assignment 3 #####\n")

# Assignment 4

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

the_points = {
  "A": 100,
  "B": 80,
  "C": 40,
  "D": 20
}

# Normal Solution

for name in students:

  print("-" * 30)

  print(f"-- Student Name => {name}")

  print("-" * 30)

  student_points = 0

  for skill in students[name]:

    print(f"- {skill} => {the_points[students[name][skill]]} Points")

    student_points += the_points[students[name][skill]]

  else:

    print(f"Total Points For {name} Is {student_points}")

# Solution With items()

for name, value in students.items():

  print("-" * 30)

  print(f"-- Student Name => {name}")

  print("-" * 30)

  student_points = 0

  for child_key, child_value in value.items():

    print(f"- {child_key} => {the_points[child_value]} Points")

    student_points += the_points[child_value]

  else:

    print(f"Total Points For {name} Is {student_points}")