#----------------------------------------------------------------
# Assignment (1)
#   Create the appropriate function that outputs all outputs in the following examples
#   The data can be increased or decreased
#----------------------------------------------------------------

def get_score (**skills) :

  for skill, value in skills.items() :

    print(f"{skill} => {value}")

get_score(math = "90%", science = "80%", language = "70%") 

print("##### End Assignment (1) #####")

#----------------------------------------------------------------
# Assignment (2)
#   Create the appropriate function that outputs all of the outputs in the following examples
#   We have new data, which is the person's name
#   The data can be increased or decreased
#   If the name is not writen, the first welcome line does not appear
#   If he does not have skills, show a message stating that he does not have a Score as in the example
#----------------------------------------------------------------

def get_people_scores(name="Unknown", **scores):
  
  if name != "Unknown":

    if len(scores) == 0:

      print(f"Hello {name} You Have No Scores To Show")

    else:

      print(f"Hello {name} This Is Your Score Table:")

  for item, value in scores.items():

    print(f"{item} => {value}")

get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")

print("\n##### End Of Assignment 2 #####\n")



#----------------------------------------------------------------
# Assignment (3)
#   Create a dictionary that contains the following data
#   Create the appropriate function that outputs all of the outputs in the following examples
#   If the name is not typed, the first welcome line does not appear
#   If he does not have the skills, show a message stating that he does not have a Score as in the example
#----------------------------------------------------------------

scores_list = {
  "Math": 90,
  "Science": 80,
  "Language": 70
}

def get_the_scores(name="Unknown", **scores):

  if name != "Unknown":

    if len(scores) == 0:

      print(f"Hello {name} You Have No Scores To Show")

    else:

      print(f"Hello {name} This Is Your Score Table:")

  for item, value in scores.items():

      print(f"{item} => {value}")

get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)

print("\n##### End Of Assignment 3 #####\n")