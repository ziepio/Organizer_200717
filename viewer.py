import PySimpleGUI as sg

#rows layout
tools_column = [
    [sg.Button('Note', button_color=('black', 'white'), size=(10, 5), key='-NOTE-')],
    [sg.Button('Business\nCard', button_color=('black', 'white'), size=(10, 5), key='-BC-')],
    [sg.Button('Discount\ncode', button_color=('black', 'white'), size=(10, 5), key='-DC-')]

]
tool_button_list = ['-NOTE-', '-BC-', '-DC-']

action_column = [
    [
        sg.Button('Add', button_color=('black', 'white'), size=(14,1), visible=False, key='-ADD-'),
        sg.Button('Remove', button_color=('black', 'white'), size=(14,1), visible=False, key='-REMOVE-')
    ],
#Note
    [sg.In('Title', visible=False, key='-TITLE-')],
    [sg.In('Content', visible=False, key='-CONTENT-')],
#BC
    [sg.In('First', visible=False, key='-FIRST-')],
    [sg.In('Last', visible=False, key='-LAST-')],
    [sg.In('Mobile', visible=False, key='-MOBILE-')],
#DC
    [sg.In('Shop', visible=False, key='-SHOP-')],
    [sg.In('Discount', visible=False, key='-DISCOUNT-')],
    [sg.In('Code', visible=False, key='-CODE-')],
#Remove
    [sg.Text('Which id number?: ', visible=False, key='-REMOVE2-')]
]
action_button_list = ['-ADD-', '-REMOVE-']


def action_column_remove():
    pass

#columns layout
layout = [
    [
        sg.Column(tools_column, size=(100, 400)),
        sg.VSeparator(),
        sg.Column(action_column, size=(450, 400))
    ]
]

window = sg.Window('Test', layout, size=(600, 400))

# def tools_button_click(event):
#     tools = ['-NOTE-', '-BC-', '-DC-']
#     window[event].update(button_color=('white', 'black'))
#     tools.remove(event)
#     for tool in tools:
#         window[tool].update(button_color=('black', 'white'))

def mark_the_selected_button(event):
    tools = ['-NOTE-', '-BC-', '-DC-']
    for tool in tools:
        window[tool].update(button_color=('black', 'white'))
    window[event].update(button_color=('white', 'black'))

def invisible_all_under_add_remove():
    actions = ['-TITLE-', '-CONTENT-', '-FIRST-', '-LAST-', '-MOBILE-', '-SHOP-', '-DISCOUNT-', '-CODE-']
    for action in actions:
        window[action].update(visible=False)

def disable_button(button_key: str):
    window[button_key].update(disabled=True)

def enable_action_buttons():
    for button in action_button_list:
        window[button].update(disabled=False)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event in ('-NOTE-', '-BC-', '-DC-'):
        chosen_tool = event
        enable_action_buttons()
        invisible_all_under_add_remove()
        mark_the_selected_button(event)
        window['-ADD-'].update(visible=True)
        window['-REMOVE-'].update(visible=True)

    if event is '-ADD-':
        disable_button('-REMOVE-')
        if chosen_tool == '-NOTE-':
            window['-TITLE-'].update(visible=True)
            window['-CONTENT-'].update(visible=True)
        elif chosen_tool == '-BC-':
            window['-FIRST-'].update(visible=True)
            window['-LAST-'].update(visible=True)
            window['-MOBILE-'].update(visible=True)
        else:
            window['-SHOP-'].update(visible=True)
            window['-DISCOUNT-'].update(visible=True)
            window['-CODE-'].update(visible=True)

    if event is '-REMOVE-':
        disable_button('-ADD-')
        window['-REMOVE2-'].update(visible=True)