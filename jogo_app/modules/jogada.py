class Jogada:
    def __init__(self, jogador, chute, jogo):
        self.jogador = jogador
        self.chute = chute
        self.jogo = jogo

    @staticmethod
    def cria(self, dados):
        try:
            jogador = dados['jogador']
            chute = dados['chute']
            jogo = dados['jogo']
            return Jogada(jogador=jogador, chute=chute, jogo=jogo)
        except Exception as e:
            print(e)
            return None

