import PySimpleGUI as sg

def telaDeLogin():
    sg.theme('Black')
    
    login = [
        [sg.Text("Usuário"), sg.Input(size= (40, 0), key= 'usuarioLogado')],
        [sg.Text("Senha  "), sg.Input(size= (40, 0), key= 'senhaLogado')],
        [sg.Checkbox("Lembre-me?", key= 'lembrar')],
        [sg.Button("Cadastrar", size= (7, -1), key= 'Cadastrar'), sg.Text(" " * 65), sg.Button("Logar", size= (5, -1), key= 'Logar')]
    ]
    janelaDeLogin = sg.Window("Login", layout= login, size= (450, 150))

    button, values = janelaDeLogin.Read()
    
    if button == 'Cadastrar':
        janelaDeLogin.close()
        telaDeCadastro()

def telaDeCadastro():
    sg.theme('Black')

    cadastro = [
        [sg.Text("Nome de Usuário"), sg.Input(size= (45, 0), key= 'usuarioCadastrar')],
        [sg.Text("Senha "), sg.Input(size= (55, 0), key= 'senhaCadastrar')],
        [sg.Text('')],
        [sg.Button("Voltar", size= (7, 0), key= 'voltarLogin'), sg.Text(' ' * 65), sg.Button("Continuar", size= (10, 0), key= 'continuarCadastro')]
    ]

    janelaDeCadastro= sg.Window("Cadastro", layout= cadastro, size= (450, 150))

    button, values = janelaDeCadastro.Read()




telaDeLogin()