import PySimpleGUI as sg

# functions
def action_read(key):
  switcher = {
    "A": "A",
    "B1": "B1",
    "B2": "B2",
    "C1": "C1",
    "C2": "C2",
  }
  return switcher.get(key, 'Exit')

# settings
font = ("Arial", 20)

# layouts / pages
layout1 = [ 
  [sg.Text('Welcome to Quiz Space', key='-text-', font=font)],
  [sg.Text('QUIZ', key='-title1-', font=("Times", 80))],
  [sg.Text('SPACE', key='-title2-', font=("Times", 80))],
  [sg.Button('Start', size=(40,1.1), font=font)],
  [sg.Button('Exit', size=(40,1.1), font=font)]
]

layout2 = [[sg.Text('This is layout 2')],
           [sg.Input(key='-IN-')],
           [sg.Input(key='-IN2-')]]

layout3 = [[sg.Text('This is layout 3 - It is all Radio Buttons')],
           *[[sg.R(f'Radio {i}', 1)] for i in range(8)]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-START-'), sg.Column(layout2, visible=False, key='-A-'), sg.Column(layout3, visible=False, key='-B1-')],
          [sg.Button('A'), sg.Button('B1'), sg.Button('Exit')]]

#STEP 2 - create the window
window = sg.Window('Quiz Space', layout, size=(500, 500), margins=(50, 50), element_justification='c')

# STEP3 - the event loop
layout = 1
current = 'START'
while True:
  event, values = window.read()   # Read the event that happened and the values dictionary
  if action_read(event) == 'Exit' :
    break
  else :
    window.FindElement(f'-{current}-').update(visible=False)
    current = action_read(event)
    window.FindElement(f'-{action_read(event)}-').update(visible=True)

window.close()
