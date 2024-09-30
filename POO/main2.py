from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e meu e-mail é:{self.email}")

gui = Cliente("Guilherme", "gui@gmail.com", 28)

#print(gui.nome, gui.email, gui.idade)
print(gui)
gui.exibir()