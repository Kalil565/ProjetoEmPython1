
import PySimpleGUI as sg
import sqlite3
import defs


dados = sqlite3.connect('teste.db')
cursor = dados.cursor()

""" cursor.execute('CREATE TABLE Usuarios("Usuario" TEXT, "Senha" TEXT, "Nome" TEXT, "Idade" INTEGER, "Endereço" TEXT,'
    '"Email" TEXT, "Trabalho" TEXT, "Estudos" TEXT, "Cursado" TEXT, "Serviço" TEXT)') """


#janela inicial
def telaDeLogin():
    sg.theme('DarkBrown')
    
    login = [
        [sg.Text('Usuário'), sg.Input(size= (40, 0), key= 'usuarioLogado')],
        [sg.Text('Senha'), sg.Input(size= (40, 0), key= 'senhaLogado')],
        [sg.Checkbox('Lembre-me?', key= 'lembrar')],
        [sg.Button('Cadastrar', size= (7, -1), key= 'Cadastrar'), sg.Text(" " * 65), sg.Button('Logar', size= (5, -1), key= 'Logar')]
    ]
    janelaDeLogin = sg.Window("Login", layout= login, size= (450, 150))

    button, values = janelaDeLogin.Read()
    
    user = values['usuarioLogado']
    senha = values['senhaLogado']

    
    if button == 'Cadastrar':
        janelaDeLogin.close()
        telaDeCadastro()
    elif button == 'Logar':
        if defs.login(user, senha):
            janelaDeLogin.close()
            telaDeInfo(user)
        else:
            janelaDeLogin.close()
            sg.popup('Erro')
            telaDeLogin()
    

#janela quando for cadastrar
def telaDeCadastro():
    sg.theme('DarkBrown')

    cadastro = [
        [sg.Text('Nome de Usuário'), sg.Input(size= (45, 0), key= 'usuarioCadastrar')],
        [sg.Text('Senha '), sg.Input(size= (55, 0), key= 'senhaCadastrar')],
        [],
        [sg.Button('Voltar', size= (7, 0), key= 'voltarLogin'), sg.Text(' ' * 65), sg.Button('Continuar', size= (10, 0), key= 'continuarCadastro')]
    ]

    janelaDeCadastro= sg.Window('Cadastro', layout= cadastro, size= (450, 150))

    button, values = janelaDeCadastro.Read()

    user= values['usuarioCadastrar']
    senha= values['senhaCadastrar']
    usuario= defs.cadastrar(user, senha)

    if button == 'voltarLogin':
        janelaDeCadastro.close()
        telaDeLogin()
    elif button == 'continuarCadastro':
        if usuario == True:
            janelaDeCadastro.close()
            inserirInfo()
        else:
            janelaDeCadastro.close()
            sg.popup("Erro")
            telaDeCadastro()

#janela para inserir os dados do usuario que está se cadastrando
def inserirInfo():
    sg.theme('DarkBrown1')

    servico= ['Programador Front-End', 'Programador Back-End', 'Programador FullStack', 'Desenvolvedor web', 'Desenvolver de Hardware']

    info = [
        [sg.Text('Nome Do Usuário; '), sg.Input(size= (80, 0), key= 'nomeDoUsuario')],
        [sg.Text('Idade; '), sg.Combo(values= list(range(1, 101)), key= 'idade', size=(5, 10), default_value= 0)],
        [sg.Text('Endereço; '), sg.Input(size= (80, 0), key= 'endereco')],
        [sg.Text('')],
        [sg.Text("E-mail; "), sg.Input(size= (80, 0), key= 'email')],
        [sg.Text("Telefone; "), sg.Input(size= (80,0), key= 'telefone')],
        [sg.Text("Você Trabalha? "), sg.Input(size= (80, 15), key= 'usuarioTrabalha')],
        [sg.Text('')],
        [sg.Text('Você ainda Estuda? '), sg.Combo(['Sim', 'Não'], key= 'estudos', size= (5, 0))],
        [sg.Text('Você é cursado? '), sg.Input(size= (80, 15), key= 'cursado')],
        [sg.Text('')],
        [sg.Text('Tipo de serviço gostaria de contratar? ', size= (25)), sg.Combo(servico, size= (20, 5), default_value= 'Nenhum', key= 'tipoDeServico')],
        [sg.Text(' ')],
        [sg.Button('Cancelar', size= (7, 0), key= 'voltarCadastro'), sg.Text(' ' * 65), sg.Button('Continuar', size= (7, 0), key= 'continuar')]    
    ]

    inserirDados = sg.Window('Inserindo Dados', layout= info, size= (550, 475))

    button, values = inserirDados.Read()

    user= []
    
    user.append(str(values['nomeDoUsuario']))
    user.append(str(values['idade']))
    user.append(str(values['endereco']))
    user.append(str(values['email']))
    user.append(str(values['telefone']))
    user.append(str(values['usuarioTrabalha']))
    user.append(str(values['estudos']))
    user.append(str(values['cursado']))
    user.append(str(values['tipoDeServico']))


    if button == 'continuar':
        semNada = 0
        for pos in range(0, len(user)):
            dados = user[pos]
            if dados == '':
                semNada += 1
        if semNada == 0:
            sg.popup("Cadastro Feito Com Sucesso")
            defs.cadastroDados(user)    
            inserirDados.close()
            telaDeLogin()
        else:
            sg.popup("Erro")
            iserirDados.close()
            inserirInfo()

    elif button == 'voltarCadastro':
        inserirDados.close()
        telaDeCadastro()



#Janela quando logar
def telaDeInfo(infos):
    sg.theme('DarkBrown1')

    
    info = defs.infoShow(infos)
    nome = info[0]

    logado = [
        [sg.Text('Usuário: '), sg.Text(f'{info[0].capitalize()}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('Idade: '), sg.Text(f'{info[1]}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('Endereço: '), sg.Text(f'{info[2].capitalize()}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('Email de Contato: '), sg.Text(f'{info[3]}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('Telefone: '), sg.Text(f'{info[4]}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('Trabalho: '), sg.Text(f'{info[5]}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('Estudos: '), sg.Text(f'{info[6]}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('Cursado: '), sg.Text(f'{info[7]}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('Tipo de serviço contratado: ', size= (25)), sg.Text(f'{info[7]}', background_color= 'Black', border_width= '3px', size= (60, 0))],
        [sg.Text('')],
        [sg.Button('Alterar', size= (7, 0), key= 'alterar'), sg.Button('Sair', size= (7, 0), key= 'deslogar')]
    ] 
    del info

    janelaDoUsuario = sg.Window("Usuário", layout=logado, size= (550, 475))

    button, values = janelaDoUsuario.Read()

    if button == 'deslogar':
        janelaDoUsuario.close()
        telaDeLogin()
    elif button == 'alterar':
        janelaDoUsuario.close()
        alteracaoDeInfo(infos, nome)


def alteracaoDeInfo(login, nome):
    sg.theme('DarkBrown1')

    loginUser = login

    servico= ['Programador Front-End', 'Programador Back-End', 'Programador FullStack', 'Desenvolvedor web', 'Desenvolver de Hardware']

    info = [
        [sg.Text('Nome Do Usuário; '), sg.Text(f'{nome}')],
        [sg.Text('Idade; '), sg.Combo(values= list(range(1, 101)), key= 'idade', size=(5, 10))],
        [sg.Text('Endereço; '), sg.Input(size= (80, 0), key= 'endereco')],
        [sg.Text('')],
        [sg.Text("E-mail; "), sg.Input(size= (80, 0), key= 'email')],
        [sg.Text("Telefone; "), sg.Input(size= (80,0), key= 'telefone')],
        [sg.Text("Você Trabalha? "), sg.Input(size= (80, 15), key= 'usuarioTrabalha')],
        [sg.Text('')],
        [sg.Text('Você ainda Estuda? '), sg.Combo(['Sim', 'Não'], key= 'estudos', size= (5, 0))],
        [sg.Text('Você é cursado? '), sg.Input(size= (80, 15), key= 'cursado')],
        [sg.Text('')],
        [sg.Text('Para qual tipo de serviço gostaria de alterar? ', size= (25)), sg.Combo(servico, size= (20, 5), key= 'tipoDeServico')],
        [sg.Text('')],
        [sg.Button('Cancelar', size= (7, 0), key= 'cancelar'), sg.Text(' ' * 65), sg.Button('Confirmar', size= (7, 0), key= 'confirmar')]    
    ]

    janelaInfo = sg.Window("Informações do Usuário", layout= info, size= (550, 475))

    button, values = janelaInfo.Read()

    usuario= []
    
    usuario.append(nome)
    usuario.append(str(values['idade']))
    usuario.append(str(values['endereco']))
    usuario.append(str(values['email']))
    usuario.append(str(values['telefone']))
    usuario.append(str(values['usuarioTrabalha']))
    usuario.append(str(values['estudos']))
    usuario.append(str(values['cursado']))
    usuario.append(str(values['tipoDeServico']))


    if button == 'confirmar':
        janelaInfo.close()
        defs.alterar(usuario)
        sg.popup('Alteração Feita com sucesso')
        telaDeInfo(loginUser)
    elif button == 'cancelar':
        janelaInfo.close()
        telaDeInfo(loginUser)


telaDeLogin()