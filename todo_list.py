import PySimpleGUI as sg

def criando_janela():
    sg.theme_background_color('#696969')
    linha = [
        # Criando uma linha inicial que vai ser uma tarefa individual
        [sg.Checkbox('', background_color='#696969', text_color='#FFA500'),
         sg.Input(font='Times 15')]
    ]
    
    # Criando o layout principal do programa
    layout = [
        [sg.Text('Todo List'.center(43), font='Times 30 bold', text_color='#FFA500',
         background_color='#696969')],
        [sg.Frame('Tarefas', layout= linha, background_color='#696969',
         title_color='#FFA500', font='Times 20 bold', key='-container-')],
        [sg.Button('Nova Tarefa', font='Times 13', button_color='black on #FFA500'),
         sg.Button('Zerar', font='Times 13', button_color='black on #FFA500')]
    ]

    return sg.Window('Developed by Airton Fabre', layout=layout,
                     finalize=True, background_color='#696969', location=(400, 100))


# ---------- Programa Principal -------------

# ---------- Criando a janela do programa -----------
window = criando_janela()

# --------- Criando as regras do programa -------------
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Nova Tarefa':
    
        # janela na posição -container- vai receber um novo checkbox mais o input
        window.extend_layout(window['-container-'],
         [[sg.Checkbox('', background_color='#696969', text_color='#FFA500'),
         sg.Input(font='Times 15')]])

        # Zerando as tarefas e reiniciando o programa
    elif event == 'Zerar':
        window.close()
        window = criando_janela()

    