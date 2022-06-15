'''Laço de repetição infinita.
Usando While true
'''

while True:
    print()
    print("######Calculadora######")
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    # operadores + - * /

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif sair == 's':
        break
    else:
        print('Operador inválido.')
    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break




