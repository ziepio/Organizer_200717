import PySimpleGUI as sg

tools_column = [
    [sg.Button('Note', button_color=('black', 'white'), enable_events=True, key='-NOTE-')],
    [sg.Button('Business Card', button_color=('black', 'white'), enable_events=True, key='-BC-')],
    [sg.Button('Discount code', button_color=('black', 'white'), enable_events=True, key='-DC-')]

]

action_column = [
    [
        sg.Button('Add', button_color=('black', 'white'), enable_events=True, key='-ADD-'),
        sg.Button('Remove', button_color=('black', 'white'), enable_events=True, key='-REMOVE-')
    ]
]

layout = [
    [
        sg.Column(tools_column),
        sg.VSeparator(),
        sg.Column(action_column)
    ]
]

window = sg.Window('Test', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break