#---------------------------------------------------------
# Assignment (1)
#   Create a folder called Python on the desktop and create a file named assign.py inside it and open it
#   Create 50 Text with name txt1, txt2, txt3 up to txt50 inside Python folder programmatically
#   Type the Elzero Web School statement => {File Number} and place File Number the file number
#   Make sure file number 25 with a name you call special-text is empty without any writing inside
#   On the first line print the Current Working Directory
#   On the second line, print the path the file is currently in
#   On the third line print the name of the currently opened file
#   On the fourth line, print all of the files inside the Python folder
#---------------------------------------------------------

file = open(r"C:\Users\ASUS\Desktop\Python\assign.py", "w")

import os

current_directory = os.getcwd()

print(current_directory)

opened_file_directory = os.path.dirname(os.path.abspath(__file__))

print(opened_file_directory)

current_file_name = os.path.basename(__file__)

print(current_file_name)

list_of_files = os.listdir(opened_file_directory)

print(len(list_of_files))


i = 1

while i < 51:

  if i == 25:

    with open(f"{opened_file_directory}\\special-text.txt", "w") as my_file:

      pass

  else:

    with open(f"{opened_file_directory}\\txt{i}.txt", "w") as my_file:

      my_file.write(f"Elzero Web School => {i}")

  i += 1

print("##### End Assignment (1) #####")

#---------------------------------------------------------
# Assignment (2)
#   Continue on the above in the first assignment
#   Open the txt1.txt file
#   Leave the first line as it says Elzero Web School => 1
#   From the beginning of the second line, type Appended => Elzero Web School fifty times each on a different line
#---------------------------------------------------------
txt1 = open(r"C:\Users\ASUS\Desktop\Python\txt1.txt", "a")

txt1.write('\n'"Appended => Elzero Web School\n" * 50)

print("##### End Assignment (2) #####")

# #---------------------------------------------------------
# Assignment (3)
#   Continue on the above in the first assignment
#   Open the txt1.txt file
#   On the first line, print the number of lines inside the file
#   On the second line, count the number of words in the file
#   In the third row, print the number of Characters in the file
#   On the fourth line, print how many times the letter "l" was found.
#---------------------------------------------------------

with open(r"c:/Users/ASUS/Desktop/Python/txt1.txt") as f:

    lines = 0

    words = 0

    characters = 0

    specific_char = 0

    for line in f:

        lines = lines + 1

        wordslist = line.split()

        words = words + len(wordslist)

        characters += sum(len(word) for word in wordslist)

        for c in line :

          if c == "l" :

            specific_char += 1

print(f"Number Of Lines Is => {lines}")

print(f"Number Of words Is => {words}")

print(f"Number Of chars Is => {characters}")

print(f"Number Of 'l' char Is => {specific_char}")


print("##### End Assignment (3) #####")

#---------------------------------------------------------
# Assignment (4)
#   Continue on the above in the first assignment
#   Programmatically and with Loop, delete the last ten txt files
#   After successfully completing the previous operation, your last file will be called txt40.txt
#---------------------------------------------------------

files = open("c:/Users/ASUS/Desktop/Python")

for i in files :

  if i == 40 :
    
    with open(f"{files}\\txt{i}", "r") as my_file:

      break

  else:
    
    with open(f"{files}\\txt{i}", "r") as my_file:

      my_file.remove(i)

  i -= 1
# لم أعرف كيفية حذف 10 ملفات عبر التكرار بعد محاولات استمرت أسبوع كامل
