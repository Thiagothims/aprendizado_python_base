from functions import calculadora

print('CALCULADORA')

print('Escolha a operação:\n'
		  'Soma{}1\n'
		  'Subtração{}2\n'
		  'Multiplicação{}3\n'
		  'Divisão{}4\n'
		  'SAIR digite 0'.format(15*'_', 10*'_', 6*'_', 12*'_' ))

operacao = 1

while operacao != 0:
	operacao = int(input('\nQual operação você quer realizar: '))
	if operacao == 0:
		print('FECHANDO...')
		break

	num1 = float(input('Digite um número: '))
	num2 = float(input('Digite um número: '))

	if operacao == 1:
		resultado = calculadora.somar(num1,num2)
	elif operacao == 2:
		resultado = calculadora.subtrair(num1,num2)
	elif operacao == 3:
		resultado = calculadora.multiplicar(num1,num2)
	elif operacao == 4:
		resultado = calculadora.dividir(num1,num2)

print('Até logo!')