#------------------------------------------------------------------------------
# Display the uniqe numbers from within the list ignoring the Strings and converting the Float to Int and Boolean as appropriate
# Remove duplicate items from within the list
# Do not print any String that you find
# If you find any Float then transfer it to Integer
# If you find True, print 1 and False instead of 0
# Sort numbers from largest to smallest
# If the number of digits is an odd number, print them as they are
# If the number of digits is even on the first line, print the sum of the first number and the last digit
# On the second line, print the sum of the second number and the penultimate number
# On the third line, print the sum of the third digit and the penultimate number
# And so on until there are only two numbers left
# The last two numbers print their product together, not add them together like the rest
#------------------------------------------------------------------------------

def get_uniques(nums):
  
    only_numbers = []  # Empty List To Contain Numbers Only

    for n in nums:

        if type(n) is int:  # Append Int Only

            only_numbers.append(n)

        elif n == True:  # Append 1 For True

            only_numbers.append(1)

        elif n == False:  # Append 0 For False

            only_numbers.append(0)

        elif type(n) == float:  # Append Int From Float

            only_numbers.append((int(n)))

    unique_nums = []  # Empty List To Contain Unique Numbers

    for i in only_numbers:

        if i not in unique_nums:  # Append Unique Numbers Only

            unique_nums.append(i)

    # Sort The Numbers From Top To Low

    unique_nums.sort(reverse=True)

    if len(unique_nums) % 2 == 0:  # Even Numbers

        even_nums = []  # Empty List For Even Numbers

        i = 0

        count = len(unique_nums)  # Unique Numbers List Length

        # Length / 2 Because Every Step Of Loop Take Two Values
        # First And Last Element

        while i < (count / 2):

            if ((count / 2) - 1) != i:

                even_nums.append(unique_nums[i] + unique_nums[count - (i + 1)])

            else:
                even_nums.append(unique_nums[i] * unique_nums[count - (i + 1)])

            i += 1  # Increse i

        for unique in even_nums:  # Loop On Even Unique Numbers

            print(unique)

    else:  # Odd Numbers

        for unique in unique_nums:  # Loop On Odd Unique Numbers

            print(unique)


get_uniques([15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 8, 9])
get_uniques([15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 3, 8, 9])

