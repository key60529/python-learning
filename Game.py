import random
import PySimpleGUI as sg


def q_list(key) :
  rules = {
    0: "5 x 5",
    1: "7 x 8",
    2: "9 x 2",
    3: "3 x 6",
    4: "4 x 9"
  }
  return rules.get(key, "1 x 1")

def a_list(key) :
  rules = {
    0: 25,
    1: 56,
    2: 18,
    3: 18,
    4: 36
  }
  return rules.get(key, 1)

abc = random.randint(0, 4)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
  [sg.Text('Please calculate and type the correct answer')],
  [sg.Text(q_list(abc)), sg.InputText()],
  [sg.Button('Ok')]
]

# Create the Window
window = sg.Window('Calculation', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
  event, values = window.read()
  if len(values[0]) > 0 and a_list(abc) == int(values[0]) :
    print('Your answer is correct')
    break
  print('Your answer incorrect. Try again.')

window.close()