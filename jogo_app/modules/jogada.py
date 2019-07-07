from jogo_app.services.segredo_service import qualifica_chute

class Jogada:
    def __init__(self, jogador, chute, jogo, qualidade=None, id=None):
        self.id = id
        self.jogador = jogador
        self.chute = chute
        self.jogo = jogo
        self.qualidade = qualidade

    def __dict__(self):
        return {
            'id': self.id,
            'jogador': self.jogador,
            'chute': self.chute,
            'jogo': self.jogo,
            'qualidade': self.qualidade
        }

    @staticmethod
    def cria(dados):
        try:
            jogador = dados['jogador']
            chute = dados['chute']
            jogo = dados['jogo']
            return Jogada(jogador=jogador, chute=chute, jogo=jogo)
        except Exception as e:
            print('Erro ao criar Jogada: ', e)
            return None
    
    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            jogador = dados[1]
            chute = dados[2]
            jogo = dados[3]
            qualidade = dados[4]
            return Jogada(jogador=jogador, chute=chute, jogo=jogo, qualidade=qualidade, id=id)
        except Exception as e:
            print('Erro ao criar Jogada de tupla: ', e)
            return None
