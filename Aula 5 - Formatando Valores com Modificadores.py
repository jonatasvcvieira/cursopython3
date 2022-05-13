'''
Formatando valores com modificadores - Aula 5

:s - Testo (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:.(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

nome = 'Jonatas vasconcelos da COSTA VieiRA'
print(nome.lower()) # tudo minúsculo
print(nome.upper()) # tudo maiúsculo
print(nome.title()) # Primeiras letras maiúculas

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{}'.format(divisao))
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print(f'{num_1:*>10}') # Completar com hashtag a esquerda
print(f'{num_1:#<10}') # Completar com hashtag a direita
print(f'{num_1:#^10}') # Completar com hashtag ao centro




