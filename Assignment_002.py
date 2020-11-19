#----------------------------------------------
#[01] Create 3 Variables Name, Age, Country
#[02] Print This Text To The Console => "Hello 'Variable Name', How You Doing \ """ Your Age Is "Variable Age""
#[03] Print The Same Previous Text But in 3 Lines Not Single Line
#[04] Get The Letter "l" From Elzero 
#[05] Get The Letter "o" From Elzero 
#[06] Get The Letters "lze" From Elzero 
#[07] Get The Letters "Ezr" From Elzero 
#[08] Get The Letters "rzE" From Elzero 
#[09] Remove Special Character From The String "#@#@Elzero#@#@" And Return Elzero
#[10] Make A Function Add Zeros Before Given Number And Return Number Not Exceed 4 Width Example "0010", "1800"
#[11] Make A Function Add Hashes Before Given String And Make Width Not Exceed 20 Characters
#[12] Convert This String "OSamA" To "osAMa"
#[13] Count How Much Word Love in This String "I Love Python And Although Love Elzero Web School"
#[14] Find The Index Of The Letter "z" in String "Elzero"
#[15] Replace The Word <3 With Love Letter One Time in This String => "I <3 Python And Although <3 Elzero Web School"
#[16] Replace All The Words <3 With Love Letter in This String => "I <3 Python And Although <3 Elzero Web School"
#[17] Format The Variables Created in Step One With The New Way f""
#----------------------------------------------


#[01] Create 3 Variables Name, Age, Country
myName = "Ayman"
myAge = 36
myContry = "Syria"

#[02] Print This Text To The Console => "Hello 'Variable Name', How You Doing \ """ Your Age Is "Variable Age""
print('''"Hello 'Ayman', How You Doing \ """ Your Age Is "36""''')

#[03] Print The Same Previous Text But in 3 Lines Not Single Line
print("Hello {:s},\nHow You Doing\"""\nYour Age Is {:d}".format (myName, myAge))

#[04] Get The Letter "l" From Elzero 
name = "Elzero"
print(name[1])

#[05] Get The Letter "o" From Elzero 
print(name[5])

#[06] Get The Letters "lze" From Elzero 
print(name[1:4])

#[07] Get The Letters "Ezr" From Elzero 
print(name[0: :2])

#[08] Get The Letters "rzE" From Elzero 
print(name[-2: :-2])

#[09] Remove Special Character From The String "#@#@Elzero#@#@" And Return Elzero
myString = "#@#@Elzero#@#@"
print (myString.strip("#@"))

#[10] Make A Function Add Zeros Before Given Number And Return Number Not Exceed 4 Width Example "0010", "1800"
tea, coffee, lemon, water = "5", "15", "115", "1115"
print(tea.zfill(4))
print(coffee.zfill(4))
print(lemon.zfill(4))
print(water.zfill(4))

#[11] Make A Function Add Hashes Before Given String And Make Width Not Exceed 20 Characters
myFunction = "Ayman"
print(myFunction.rjust(15,"#"))

#[12] Convert This String "OSamA" To "osAMa"
teacher = "OSamA"
print(teacher.swapcase())

#[13] Count How Much Word Love in This String "I Love Python And Although Love Elzero Web School"
fact = "I Love Python And Although Love Elzero Web School"
print(fact.count("Love"))

#[14] Find The Index Of The Letter "z" in String "Elzero"
print(name.index('z'))

#[15] Replace The Word <3 With Love Letter One Time in This String => "I <3 Python And Although <3 Elzero Web School"
print(fact.replace("Love","<3",1))

#[16] Replace All The Words <3 With Love Letter in This String => "I <3 Python And Although <3 Elzero Web School"
anotherFact = "I <3 Python And Although <3 Elzero Web School"
print(anotherFact.replace("<3","Love",2))

myName = "Ayman"
myAge = 36
myContry = "Syria"
#[17] Format The Variables Created in Step One With The New Way f""
print(f"myName Is: {myName} and my Age Is: {myAge}")
