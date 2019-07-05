import sqlite3

def cria():
    conexao = sqlite3.connect("jogo_senha.db")
    try:
        cursor = conexao.cursor()
        cursor.execute("CREATE Table IF NOT EXISTS Usuario( \
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            nome TEXT NOT NULL, \
            email TEXT NOT NULL, \
            google_id TEXT NOT NULL \
        );")
        conexao.commit()
        cursor.execute("CREATE Table IF NOT EXISTS Jogo( \
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            jogador1 INTEGER NOT NULL, \
            jogador2 INTEGER, \
            segredo1 TEXT NOT NULL, \
            segredo2 TEXT NOT NULL, \
            turno INTEGER NOT NULL, \
            FOREIGN KEY(jogador1) REFERENCES Usuario(id), \
            FOREIGN KEY(jogador2) REFERENCES Usuario(id), \
            FOREIGN KEY(turno) REFERENCES Usuario(id) \
        );")
        conexao.commit()
        cursor.execute("CREATE Table IF NOT EXISTS Jogada( \
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            jogo INTEGER NOT NULL, \
            jogador INTEGER NOT NULL, \
            chute INTEGER NOT NULL, \
            FOREIGN KEY(jogo) REFERENCES Jogo(id), \
            FOREIGN KEY(jogador) REFERENCES Usuario(id) \
        );")
        conexao.commit()
    except Exception as e:
        print('Alerta ao criar banco: ', e)
    finally:
        cursor.close()
        conexao.close()

def deleta():
    conexao = sqlite3.connect("jogo_senha.db")
    try:
        cursor = conexao.cursor()
        cursor.execute("DROP Table IF EXISTS Usuario;")
        conexao.commit()
        cursor.execute("DROP Table IF EXISTS Jogo;")
        conexao.commit()
        cursor.execute("DROP Table IF EXISTS Jogada;")
        conexao.commit()
    except Exception as e:
        print('Alerta ao deletar banco: ', e)
    finally:
        cursor.close()
        conexao.close()

if __name__ == '__main__':
    opcao = input("Deseja criar(1) ou deletar(0) o banco ?")
    if opcao == '0':
        deleta()
    elif opcao == '1':
        cria()
    else:
        print("Opcao invalida! Execute novamente.")
