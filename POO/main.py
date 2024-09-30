class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir(self):
        print(self.nome, self.email)

guilherme = Cliente("Guilherme", "guilherme@gmail.com")

#print(guilherme)
#print(guilherme.nome)
#print(guilherme.email)

guilherme.exibir()