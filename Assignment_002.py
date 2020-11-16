
myName = "Ayman"
myAge = 36
myContry = "Syria"

print("Hello {:s}, How You Doing\""" Your Age Is {:d}".format (myName, myAge))

print("Hello {:s},\nHow You Doing\"""\nYour Age Is {:d}".format (myName, myAge))

name = "Elzero"
print (name[1])
print (name[5])
print (name[1:4])
print (name[0: :2])
print (name[-2: :-2])

myString = "#@#@Elzero#@#@"
print (myString.strip("#@"))

tea, coffee, lemon, water = "5", "15", "115", "1115"
print (tea.zfill(4))
print (coffee.zfill(4))
print (lemon.zfill(4))
print (water.zfill(4))

myFunction = "Ayman"
print (myFunction.rjust(15,"#"))

teacher = "OSamA"
print (teacher.swapcase())

fact = "I Love Python And Although Love Elzero Web School"
print (fact.count("Love"))

print(name[2])

print(fact.replace("Love","<3",1))

anotherFact = "I <3 Python And Although <3 Elzero Web School"
print(anotherFact.replace("<3","Love",2))

myName = "Ayman"
myAge = 36
myContry = "Syria"

print(f"myName Is: {myName} and my Age Is: {myAge}")
