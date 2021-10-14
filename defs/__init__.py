import sqlite3

usuario = sqlite3.connect('teste.db')
cursor = usuario.cursor()
cursor.execute('SELECT * FROM teste')
dados = cursor.fetchall()


def login(login, senha):
    for pos in range(0, len(dados)):
        info = dados[pos]
        if info[0] == login:
            if info[1] == senha:
                return True
    else:
        return False

def infoShow(login = 'kalil565'):
    infos = []
    for posUser in range(0, len(dados)):
        user = dados[posUser]
        if login == user[0]:
            cursor.execute('SELECT * FROM dados')
            userInfo= cursor.fetchall()
            for posInfo in range(0, len(userInfo)):
                if posInfo == posUser:
                    infos = userInfo[posInfo]
                    return infos


def cadastrar(user= '', senha= ''):
    if user != '':
        if senha != '':
            cursor.execute('INSERT INTO teste VALUES("'+user+'", "'+senha+'")')
            usuario.commit()
            return True


def cadastroDados(dadosUser= list()):
    if len(dadosUser) == 9:
        cursor.execute('INSERT INTO dados VALUES("'+dadosUser[0]+'", "'+dadosUser[1]+'", "'+dadosUser[2]+'",'
        ' "'+dadosUser[3]+'", "'+dadosUser[4]+'", "'+dadosUser[5]+'", "'+dadosUser[6]+'", "'+dadosUser[7]+'", "'+dadosUser[8]+'")')
        usuario.commit()
        return True
        
def alterar(dadosUser= list()):
    for pos in range(0, len(dados)):
        user= dados[pos]
        for posUser in range(0, len(user)):
            if user[posUser][0] == dadosUser[0]:
                if user[posUser][1] != dadosUser[1] != '':
                    cursor.execute('UPDATE dados SET Idade= "'+dadosUser[1]+'" WHERE Nome = "'+dadosUser[0]+'"')
                    usuario.commit()
                if user[posUser][2] != dadosUser[2] != '':
                    cursor.execute('UPDATE dados SET Endereço= "'+dadosUser[2]+'" WHERE Nome = "'+dadosUser[0]+'"')
                    usuario.commit()
                if user[posUser][3] != dadosUser[3] != '':
                    cursor.execute('UPDATE dados SET Email= "'+dadosUser[3]+'" WHERE Nome = "'+dadosUser[0]+'"')
                    usuario.commit()
                if user[posUser][4] != dadosUser[4] != '':
                    cursor.execute('UPDATE dados SET Telefone= "'+dadosUser[4]+'" WHERE Nome = "'+dadosUser[0]+'"')
                    usuario.commit()
                if user[posUser][5] != dadosUser[5] != '':
                    cursor.execute('UPDATE dados SET Trabalho= "'+dadosUser[5]+'" WHERE Nome = "'+dadosUser[0]+'"')
                    usuario.commit()
                if user[posUser][6] != dadosUser[6] != '':
                    cursor.execute('UPDATE dados SET Estudo= "'+dadosUser[6]+'" WHERE Nome = "'+dadosUser[0]+'"')
                    usuario.commit()
                if user[posUser][7] != dadosUser[7] != '':  
                    cursor.execute('UPDATE dados SET Cursado= "'+dadosUser[7]+'" WHERE Nome = "'+dadosUser[0]+'"')
                    usuario.commit()
                if user[posUser][8] != dadosUser[8] != '':  
                    cursor.execute('UPDATE dados SET Serviço= "'+dadosUser[8]+'" WHERE Nome = "'+dadosUser[0]+'"')
                    usuario.commit()
                return True