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

counter = 3

for num in my_nums :

  if num % 5 == 0 :

    print(f"{counter} => {num}")
    
    counter -= 1

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

my_rank = {

  "Math" : 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'

}
A = 100
B = 80
C = 40

for rank_key, rank_value in my_rank.items() :

  print(f"My Rank in {rank_key} Is: {rank_value} And This Equal", end = " ")

  if rank_value == "A" :

    print("100 points")

  elif rank_value == "B" :

    print("80 points")

  else:

    print("40 points")

sum = A + B + A + C

print(f"'Total Points Is {sum}")