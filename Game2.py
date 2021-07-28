import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout1 = [
  [sg.Text('Please enter your name'), sg.InputText()],
  [sg.Button('Next')]
]

layout2 = [
  [sg.Text('Please choose your gender')]
  [sg.Button('Boy'), sg.Button('Girl')]
]

layout = [[sg.Column(layout1, key='-START-'), sg.Column(layout2, visible=False, key='-A-'), sg.Column(layout3, visible=False, key='-B1-')],
          [sg.Button('A'), sg.Button('B1'), sg.Button('Exit')]]

# Create the Window
window = sg.Window('Your Name', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
  event, values = window.read()
  if len(values[0]) > 0 :
    print('Your name is ', values[0])
    break
  print('Please input something.')

window.close()