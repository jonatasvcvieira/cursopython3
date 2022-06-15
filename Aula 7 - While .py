"""

while em Python
Utilizado para relizar ações enquanto uma condição for verdadeira.
Requisitos: Entender condições e opeadores
"""

"""
while True: # loop infinito
    nome = input("Qual é o seu nome?")
    print(f'Olá {nome}!')

print('Não será executada.')

"""
"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        #continue
        break

    print(x)
    x = x + 1
print('Acabou!')
"""


x = 0 # x = coluna
while x < 10:
     y = 0 # y = linha

     while y < 5:
         print(f'({x};{y})')
         y += 1 # y = y + 1

     x += 1 # x = x 1

print('Acabou!')

