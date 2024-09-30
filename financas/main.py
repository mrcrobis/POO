from utilitarios import cadastrar_categoria, cadastrar_transacao, saldo_total
from transacao import Transacao
# categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas Fixas')
categoria_viagens = cadastrar_categoria('Viagens')
categoria_lazer = cadastrar_categoria('Lazer')

# transacoes
cadastrar_transacao('Salário', 1628.55, '21/01/2024', categoria_receitas)
cadastrar_transacao('Mesada', 200.0, '29/01/2024', categoria_receitas)
cadastrar_transacao('Ingresso cinema', -40.0, '16/01/2024', categoria_lazer)
cadastrar_transacao('Conta de luz', -282.84, '14/01/2024', categoria_contas)
cadastrar_transacao('Disney', -475.0, '14/01/2024', categoria_viagens)

total = saldo_total()

print('Saldo total: ', total)