import sqlite3

usuario = sqlite3.connect('teste.db')
cursor = usuario.cursor()
cursor.execute('SELECT * FROM teste')
dados = cursor.fetchall()

def login(login= '', senha= ''):
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
