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

def get_people_scores (name, **scores) :

  if not scores:

    print(f"Hello {name} You Have No Scores To Show")

  elif not name :

    for skill, value in scores.items() :

      print(f"{skill} => {value}")

  else:

    print(f"Hello {name} This Is Your Scores Table: ")

    for skill, value in scores.items() :

      print(f"{skill} => {value}")



get_people_scores("Ayman", Math="90", Science="80", Language="70")
get_people_scores("Salah", Logic=50, Go=40)
get_people_scores(None, problem=65, DataScience=60)
get_people_scores("Ayman")

print("##### End Assignment (2) #####")



#----------------------------------------------------------------
# Assignment (3)
#   Create a dictionary that contains the following data
#   Create the appropriate function that outputs all of the outputs in the following examples
#   If the name is not typed, the first welcome line does not appear
#   If he does not have the skills, show a message stating that he does not have a Score as in the example
#----------------------------------------------------------------

scores_list = {

  "Math" : "90",

  "Science" : "80",

  "Language" : "70"

}

def get_the_scores (name, **scores_list) :
  if not scores_list :
    print(f"Hello {name} You Have No Scores To Show")
  elif not name :
    for skill, value in scores_list.items() :
      print(f"{skill} => {value}")
  else :
    print(f"Hello {name} This Is Your Score Table: ")
    for skill, value in scores_list.items() :
      print(f"{skill} => {value}")

get_the_scores("Ayman", **scores_list)
get_the_scores("name")
get_the_scores(None, **scores_list)