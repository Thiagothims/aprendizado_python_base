class retorna_condicao_do_investimento:

    def __init__(self, real, esperado):
        self.real = real
        self.esperado = esperado

    def investimento(self, real, esperado):
        if real > esperado:
            print('Ótima aplicação!')
        elif real == esperado:
            print('Não há percentual de lucro.')
        elif real > esperado:
            print('Não invista seu capital, pois este investimento é prejuízo certo!')