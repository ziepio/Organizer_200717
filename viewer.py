import PySimpleGUI as sg

tool_button_list = ['-NOTE-', '-BC-', '-DC-']
tools_column = [
    [sg.Button('Note', button_color=('black', 'white'), size=(10, 5), pad=((0, 0), (35, 10)), key='-NOTE-')],
    [sg.Button('Business\nCard', button_color=('black', 'white'), size=(10, 5), pad=((0, 0), (10, 10)), key='-BC-')],
    [sg.Button('Discount\ncode', button_color=('black', 'white'), size=(10, 5), pad=((0, 0), (10, 35)), key='-DC-')]
]

layout1 = [
    [
        sg.Button('Add', button_color=('black', 'white'), size=(14, 1), pad=((70, 25), (0, 0)), key='-ADD1-'),
        sg.Button('Remove', button_color=('black', 'white'), size=(14, 1), pad=((25, 70), (0, 0)), key='-REMOVE1-')
    ],
    [sg.Text('Title:', visible=False, pad=((0, 0), (12, 0)), key='-TITLE_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-TITLE-')],
    [sg.Text('Content:', visible=False, pad=((0, 0), (6, 0)), key='-CONTENT_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-CONTENT-')],
    [sg.Text('Note ID to be removed:', visible=False, pad=((0, 0), (6, 0)), key='-ID_REMOVE1_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-ID_REMOVE1-')],
    [sg.Button('Submit', visible=False, size=(14,1), pad=(150, (12, 0)), key='-SUBMIT1-')]
]

layout2 = [
    [
        sg.Button('Add', button_color=('black', 'white'), size=(14, 1), pad=((70, 25), (0, 0)), key='-ADD2-'),
        sg.Button('Remove', button_color=('black', 'white'), size=(14, 1), pad=((25, 70), (0, 0)), key='-REMOVE2-')
    ],
    [sg.Text('First:', visible=False, pad=((0, 0), (12, 0)), key='-FIRST_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-FIRST-')],
    [sg.Text('Last:', visible=False, pad=((0, 0), (6, 0)), key='-LAST_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-LAST-')],
    [sg.Text('Mobile:', visible=False, pad=((0, 0), (6, 0)), key='-MOBILE_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-MOBILE-')],
    [sg.Text('Business Card ID to be removed:', visible=False, pad=((0, 0), (6, 0)), key='-ID_REMOVE2_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-ID_REMOVE2-')],
    [sg.Button('Submit', visible=False, size=(14,1), pad=(150, (12, 0)), key='-SUBMIT2-')]
]

layout3 = [
    [
        sg.Button('Add', button_color=('black', 'white'), size=(14, 1), pad=((70, 25), (0, 0)), key='-ADD3-'),
        sg.Button('Remove', button_color=('black', 'white'), size=(14, 1), pad=((25, 70), (0, 0)), key='-REMOVE3-')
    ],
    [sg.Text('Shop:', visible=False, pad=((0, 0), (12, 0)), key='-SHOP_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-SHOP-')],
    [sg.Text('Discount:', visible=False, pad=((0, 0), (6, 0)), key='-DISCOUNT_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-DISCOUNT-')],
    [sg.Text('Code:', visible=False, pad=((0, 0), (6, 0)), key='-CODE_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-CODE-')],
    [sg.Text('Discount code ID to be removed:', visible=False, pad=((0, 0), (6, 0)), key='-ID_REMOVE3_DESC-'),
     sg.In('', visible=False, size=(62, 1), pad=(0, 0), key='-ID_REMOVE3-')],
    [sg.Button('Submit', visible=False, size=(14,1), pad=(150, (12, 0)), key='-SUBMIT3-')]
]

layout = [
    [
        sg.Column(tools_column, size=(100, 400)),
        sg.VSeparator(),
        sg.Column(layout1, size=(450, 400), visible=False, key='-LAYOUT1-'),
        sg.Column(layout2, size=(450, 400), visible=False, key='-LAYOUT2-'),
        sg.Column(layout3, size=(450, 400), visible=False, key='-LAYOUT3-')
    ]
]

window = sg.Window('Organizer v1.0', layout, size=(600, 400))


def return_to_start_settings():
    actions = ['-TITLE_DESC-', '-TITLE-', '-CONTENT_DESC-', '-CONTENT-', '-ID_REMOVE1_DESC-', '-ID_REMOVE1-',
               '-SUBMIT1-', '-FIRST_DESC-', '-FIRST-', '-LAST_DESC-', '-LAST-', '-MOBILE_DESC-', '-MOBILE-',
               '-ID_REMOVE2_DESC-', '-ID_REMOVE2-', '-SUBMIT2-', '-SHOP_DESC-', '-SHOP-', '-DISCOUNT_DESC-',
               '-DISCOUNT-', '-CODE_DESC-', '-CODE-', '-ID_REMOVE3_DESC-', '-ID_REMOVE3-', '-SUBMIT3-']
    action_button_list = ['-ADD1-', '-ADD2-', '-ADD3-', '-REMOVE1-', '-REMOVE2-', '-REMOVE3-']
    layout_list = ['-LAYOUT1-', '-LAYOUT2-', '-LAYOUT3-']
    for action in actions:
        window[action].update(visible=False)
    for action_button in action_button_list:
        window[action_button].update(disabled=False)
    for each_layout in layout_list:
        window[each_layout].update(visible=False)


def enable_button(button_key: str):
    window[button_key].update(disabled=False)

def disable_button(button_key: str):
    window[button_key].update(disabled=True)

def mark_the_selected_button(event):
    tools = ['-NOTE-', '-BC-', '-DC-']
    for tool in tools:
        window[tool].update(button_color=('black', 'white'))
    window[event].update(button_color=('white', 'black'))

def select_layout(event):
    act_col_dict = {'-NOTE-': '-LAYOUT1-', '-BC-': '-LAYOUT2-', '-DC-': '-LAYOUT3-'}
    window[act_col_dict[event]].update(visible=True)

def set_visibility(chosen_tool: str, on_off: bool):
    dict_tools = {'-NOTE-': ['-TITLE_DESC-', '-TITLE-', '-CONTENT_DESC-', '-CONTENT-', '-SUBMIT1-'],
                  '-BC-': ['-FIRST_DESC-', '-FIRST-', '-LAST_DESC-', '-LAST-', '-MOBILE_DESC-', '-MOBILE-',
                           '-SUBMIT2-'],
                  '-DC-': ['-SHOP_DESC-', '-SHOP-', '-DISCOUNT_DESC-', '-DISCOUNT-', '-CODE_DESC-', '-CODE-',
                           '-SUBMIT3-']}
    for tool in dict_tools[chosen_tool]:
        window[tool].update(visible=on_off)
    if on_off is False:
        window[f'-SUBMIT{dict_tools[chosen_tool][-1][-2]}-'].update(visible=True)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event in ('-NOTE-', '-BC-', '-DC-'):
        chosen_tool = event
        return_to_start_settings()
        mark_the_selected_button(event)
        select_layout(event)

    if event in ('-ADD1-', '-ADD2-', '-ADD3-'):
        enable_button(f'-REMOVE{event[-2]}-')
        disable_button(event)
        if chosen_tool in ('-NOTE-', '-BC-', '-DC-'):
            set_visibility(chosen_tool, True)
            window[f'-ID_REMOVE{event[-2]}_DESC-'].update(visible=False)
            window[f'-ID_REMOVE{event[-2]}-'].update(visible=False)

    if event in ('-REMOVE1-', '-REMOVE2-', '-REMOVE3-'):
        enable_button(f'-ADD{event[-2]}-')
        disable_button(event)
        if chosen_tool in ('-NOTE-', '-BC-', '-DC-'):
            set_visibility(chosen_tool, False)
            window[f'-ID_REMOVE{event[-2]}_DESC-'].update(visible=True)
            window[f'-ID_REMOVE{event[-2]}-'].update(visible=True)