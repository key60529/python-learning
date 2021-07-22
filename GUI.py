import PySimpleGUI as sg

# settings
font = ("Arial", 20)

# layouts / pages
layout = [ 
  [sg.Text('Welcome to Quiz Space', key='-text-', font=font)],
  [sg.Text('QUIZ', key='-title1-', font=("Times", 80))],
  [sg.Text('SPACE', key='-title2-', font=("Times", 80))],
  [sg.Button('Start', size=(40,1.1), font=font)],
  [sg.Button('Exit', size=(40,1.1), font=font)]
]

#STEP 2 - create the window
window = sg.Window('Quiz Space', layout, size=(500, 500), margins=(50, 50), element_justification='c')

# STEP3 - the event loop
while True:
  event, values = window.read()   # Read the event that happened and the values dictionary
  print(event, values)
  if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
      break
  if event == 'Button':
    print('You pressed the button')
window.close()