from functions import retorna_condicao_do_investimento

capital = float(input('Valor do Capital: R$ '))
taxa = float(input('Taxa: ')) #valor percentual decimal ex: 0.1 == 10%
prazo = int(input('Prazo (dias, meses, anos:'))
rendimento_esperado = float(input('Rendimento esperado: R$ '))

rendimento_real = (capital*(1+taxa)**prazo)-capital
print('Valor do rendimento real: R$ {:.2f}'.format(rendimento_real))

resultado_investimento = retorna_condicao_do_investimento(rendimento_real,rendimento_esperado)
print(resultado_investimento)
