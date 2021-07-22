# Switch example
def askInput():
  return input("Please choose Boy / Girl: ")

def checkInput(gender):
  switcher = {
    "Boy": "You are a boy",
    "Girl": "You are a girl",
  }
  return switcher.get(gender, askInput())

gender = askInput()
print(checkInput(gender))
