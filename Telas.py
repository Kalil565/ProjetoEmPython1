import PySimpleGUI as sg


#janela inicial
def telaDeLogin():
    sg.theme('DarkBrown')
    
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



#janela quando for cadastrar
def telaDeCadastro():
    sg.theme('DarkBrown')

    cadastro = [
        [sg.Text("Nome de Usuário"), sg.Input(size= (45, 0), key= 'usuarioCadastrar')],
        [sg.Text("Senha "), sg.Input(size= (55, 0), key= 'senhaCadastrar')],
        [],
        [sg.Button("Voltar", size= (7, 0), key= 'voltarLogin'), sg.Text(' ' * 65), sg.Button("Continuar", size= (10, 0), key= 'continuarCadastro')]
    ]

    janelaDeCadastro= sg.Window("Cadastro", layout= cadastro, size= (450, 150))

    button, values = janelaDeCadastro.Read()

    if button == 'voltarLogin':
        janelaDeCadastro.close()
        telaDeLogin()
    elif button == 'continuarCadastro':
        janelaDeCadastro.close()
        inserirInfo()


#janela para inserir os dados do usuario que está se cadastrando
def inserirInfo():
    sg.theme('DarkBrown1')

    servico= ['Programador Front-End', 'Programador Back-End', 'Programador FullStack', 'Desenvolvedor web', 'Desenvolver de Hardware']

    info = [
        [sg.Text("Nome Do Usuário; ", size= (15)), sg.Input(size= (60, 0), key= 'nomeDoUsuario')],
        [sg.Text("Idade; "), sg.Combo(values= list(range(1, 101)), key= 'idade', size=(5, 10), default_value= 0)],
        [sg.Text("Endereço; ", size= (15))],
        [sg.Input(size= (60, 0), key= 'endereco')],
        [sg.Text('')],
        [sg.Text("E-mail; ", size= (15)), sg.Input(size= (60, 0), key= 'email')],
        [sg.Text("Telefone; ", size= (15)), sg.Input(size= (60,0), key= 'telefone')],
        [sg.Text("Você Trabalha? ")],
        [sg.Input(size= (60, 15), key= 'usuarioTrabalha')],
        [sg.Text('')],
        [sg.Text("Você ainda Estuda?"), sg.Combo(['Sim', 'Não'], key= 'estudos', size= (5, 0))],
        [sg.Text("Você é cursado? ", size= (15))],
        [sg.Input(size= (60, 15), key= 'cursado')],
        [sg.Text('')],
        [sg.Text("Tipo de serviço gostaria de contratar? ", size= (15)), sg.Combo(servico, size= (20, 5), default_value= 'Nenhum', key= 'tipoDeServico')],
        [sg.Text(' ')],
        [sg.Button("Cancelar", size= (7, 0), key= 'voltarCadastro'), sg.Text(' ' * 65), sg.Button("Continuar", size= (7, 0), key= 'continuar')]    
    ]

    inserirDados = sg.Window("Inserindo Dados", layout= info, size= (450, 600))

    button, values = inserirDados.Read()

    if button == 'voltarCadasrto':
        inserirDados.close()
        telaDeCadastro()
    elif button == 'continuar':
        inserirDados.close()
        telaDeLogin()



#Janela quando logar
def janelaLogada():
    sg.theme('DarkBrown1')

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