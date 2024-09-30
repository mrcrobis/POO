from categoria import Categoria
from transacao import Transacao

LISTA_CATEGORIAS = []
LISTA_TRANSACOES = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome)

    LISTA_CATEGORIAS.append(nova_categoria)

    return nova_categoria

def cadastrar_transacao(descricao, valor, data, categoria):
    nova_transacao = Transacao(descricao, valor, data, categoria)

    LISTA_TRANSACOES.append(nova_transacao)

    return nova_transacao

def saldo_total():
    total = 0

    for t in LISTA_TRANSACOES:
        total += t.valor

    return total