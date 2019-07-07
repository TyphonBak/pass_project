from jogo_app.modules.jogada import Jogada
from jogo_app.services.segredo_service import gera_segredo

class Jogo:
    def __init__(self, jogador1, jogador2=None, id=None, segredo1=None, segredo2=None):
        self.id = id
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.segredo1 = segredo1
        self.segredo2 = segredo2
        self.turno = jogador1

    def mudaTurno(self):
        self.turno = self.jogador1 if self.turno == self.jogador2 else self.jogador2

    def faz_jogada(self, jogador, chute):
        if self.turno == jogador:
            dados = { 'jogador': jogador, 'chute': chute, 'jogo': self.id}
            jogada = Jogada.cria(dados)
            if self.jogador2 != None:
                self.mudaTurno()
            return jogada
        return None

    def acertou(self, jogada):
        if jogada.jogador == self.jogador1 and jogada.chute == self.segredo2:
            return True
        elif jogada.jogador == self.jogador2 and jogada.chute == self.segredo1:
            return True
        return False

    def finaliza_jogo(self):
        self.turno = None

    def define_segredo(self, jogador, segredo):
        if jogador==self.jogador1 and segredo!=None:
            self.segredo1 = segredo
        elif jogador==self.jogador2:
            self.segredo2 = segredo
        elif jogador == self.jogador1 and segredo == None:
            self.segredo2 = gera_segredo()

    def __dict__(self):
        return {
            'id': self.id,
            'jogador1': self.jogador1,
            'jogador2': self.jogador2,
            'segredo1': self.segredo1,
            'segredo2': self.segredo2,
            'turno': self.turno
        }

    @staticmethod
    def cria(dados):
        try:
            jogador1 = dados['jogador1']
            jogador2 = dados.get('jogador2')
            segredo2 = dados.get('segredo2')
            id = dados.get('id')
            return Jogo(jogador1, jogador2, segredo2=segredo2, id=id)
        except Exception as e:
            print('Alerta ao criar jogo¹: ', e)
            return None

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            jogador1 = dados[1]
            jogador2 = dados[2]
            segredo1 = dados[3]
            segredo2 = dados[4]
            turno = dados[5]
            jogo = Jogo(jogador1=jogador1, jogador2=jogador2, id=id, segredo1=segredo1, segredo2=segredo2)
            jogo.turno=turno
            return jogo
        except Exception as e:
            print('Alerta ao criar jogo²: ', e)
            return None