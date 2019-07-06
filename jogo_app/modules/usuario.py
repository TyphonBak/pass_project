class Usuario:
    def __init__(self, google_id, nome, email, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.google_id = google_id

    def __dict__(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'google_id': self.google_id
        }

    @staticmethod
    def cria(dados):
        try:
            google_id = dados.get('google_id')
            nome = dados.get('nome')
            email = dados.get('email')
            if None in [google_id, nome, email]:
                return None
            return Usuario(google_id=google_id, nome=nome, email=email)
        except Exception as e:
            return None
    
    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            nome = dados[1]
            email = dados[2]
            google_id = dados[3]
            return Usuario(google_id=google_id, nome=nome, email=email, id=id)
        except Exception as e:
            return None
