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

def cadastrar(user= '', senha= ''):
    cursor.execute('INSERT INTO teste VALUES("'+user+'", "'+senha+'")')
    usuario.commit()

def cadastroDados(dadosUser= list()):
    if len(dadosUser) == 9:
        cursor.execute('INSERT INTO dados VALUES("'+dadosUser[0]+'", "'+dadosUser[1]+'", "'+dadosUser[2]+'",'
        ' "'+dadosUser[3]+'", "'+dadosUser[4]+'", "'+dadosUser[5]+'", "'+dadosUser[6]+'", "'+dadosUser[7]+'", "'+dadosUser[8]+'")')
        usuario.commit()
        return True