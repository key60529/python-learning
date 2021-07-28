# functions
def ask_input(text) :
  return input(text)

def check_gender(gender) :
  rules = {
    "Boy": True,
    "Girl": True,
    "boy": True,
    "girl": True
  }
  return rules.get(gender, False)

def check_mode(mode) :
  rules = {
    "Classic": True,
    "Creative": True,
    "Ranked": True
  }
  return rules.get(mode, False)


# game main()
print("Welcome to PUBG!")
name = ask_input("What's your name: ")
age = int(ask_input("Age: "))

if age < 17 : 
  print("Younger than 18 cannot play this game")
else :
  gender = ask_input("Boy or girl: ")
  while not check_gender(gender) :
    gender = ask_input("Please choose Boy or girl only: ")
    
  # gender = ask_input("Boy or girl: ")

  # != not equal
  # == equal
  # if gender != "Boy" and gender != "girl": 
    # gender = ask_input("Please type Boy or girl only: ")

  mode = ask_input("Classic / Creative / Ranked: ")
  while not check_mode(mode) :
    mode = ask_input("Please choose Classic / Creative / Ranked only: ")

  print("Character(" + gender + "): " + name)
  print("Queuing in " + mode + " mode")