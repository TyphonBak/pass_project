class Usuario:
    def __init__(self, token, nome, email, id=None):
        self.token = token
        self.nome = nome
        self.email = email
        self.google_id = None

    @set
    def id(self, google_id):
        self.google_id = google_id

    @staticmethod
    def cria(self, dados):
        try:
            token = dados['token']
            nome = dados['nome']
            email = dados['email']
            return Usuario(token=token, nome=nome, email=email)
        except Exception as e:
            return None
    
    @staticmethod
    def cria_de_tupla(self, dados):
        try:
            id = dados['id']
            token = dados['token']
            nome = dados['nome']
            email = dados['email']
            return Usuario(token=token, nome=nome, email=email, id=id)
        except Exception as e:
            return None
