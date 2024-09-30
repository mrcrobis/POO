from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    descricao: str
    valor: float
    data: str
    categoria: Categoria

    def exibir(self):
        print(f'DESCRICAO: {self.descricao} | VALOR: {self.valor} | DATA: {self.data} | CATEGORIA: {self.categoria.nome}')