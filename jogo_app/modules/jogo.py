from jogo_app.modules.jogada import Jogada

class Jogo:
    def __init__(self, jogador1, jogador2=None, id=None):
        self.id = id
        self.jogador1 = jogador1
        self.segredo_j1 = None
        self.jogador2 = jogador2
        self.segredo_j2 = None
        self.turno = self.jogador1

    def mudaTurno(self):
        self.turno = self.jogador1 if self.turno == self.jogador2 else self.jogador2

    def fazJogada(self, jogador, chute):
        if self.turno == jogador:
            dados = { 'jogador': jogador, 'chute': chute, 'jogo': self}
            jogada = Jogada.cria(dados)
            if self.jogador2 != None:
                self.mudaTurno()
            return jogada
        return None

    def acertou(self, jogada):
        if jogada.jogador == self.jogador1 and jogada.chute == self.segredo_j2:
            return True
        elif jogada.jogador == self.jogador2 and jogada.chute == self.segredo_j1:
            return True
        return False

    def finaliza_jogo(self):
        self.turno = None

    def define_segredo(self, jogador, segredo):
        if jogador==self.jogador1:
            self.segredo_j1 = 1234
        elif jogador==self.jogador2:
            self.segredo_j2 = segredo

    @staticmethod
    def cria(dados):
        try:
            jogador1 = dados['jogador1']
            jogador2 = dados.get('jogador2')
            return Jogo(jogador1, jogador2)
        except Exception as e:
            print('Alerta ao criar jogo¹: ', e)
            return None

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            jogador1 = dados[1]
            jogador2 = dados[2]
            return Jogo(jogador1, jogador2, id)
        except Exception as e:
            print('Alerta ao criar jogo²: ', e)
            return None