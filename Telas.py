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
    if button == 'Logar':
        janelaDeLogin.close()
        janelaLogada()


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

    if button == 'voltarLogin':
        janelaDeCadastro.close()
        telaDeLogin()

def janelaLogada():
    sg.theme('Black')

    logado = [
        [sg.Text("Usuário: ", size= (10, 5)), sg.Text(" ", size= (10, 5))],
        [sg.Button("Alterar", size= (7, 0))],
        [sg.Button("Sair", size= (7, 0), key= 'deslogar')]

    ]

    janelaDoUsuario = sg.Window("Usuário", layout= logado, size= (400, 600))

    button, values = janelaDoUsuario.Read()

    if button == 'deslogar':
        janelaDoUsuario.close()
        telaDeLogin()

telaDeLogin()