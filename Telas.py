import PySimpleGUI as sg

def telaDeLogin():
    sg.theme('Black')
    
    login = [
        [sg.Text("Usuário"), sg.Input(size= (40, 0), key= 'usuarioLogado')],
        [sg.Text("Senha  "), sg.Input(size= (40, 0), key= 'senhaLogado')],
        [sg.Button("Cadastrar", size= (7, -1), key= 'Cadastrar'), sg.Text(" " * 55), sg.Button("Logar", size= (5, -1), key= 'Logar')]
    ]
    janelaDeLogin = sg.Window("Login", layout= login, size= (400, 150))

    button, values = janelaDeLogin.Read()



telaDeLogin()
