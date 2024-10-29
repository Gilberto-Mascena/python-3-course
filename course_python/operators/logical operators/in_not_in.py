# Operadores lógicos in e not in
# Strings são iteráveis, ou seja, podemos percorrer cada caractere de uma string.
# O operador in verifica se um determinado caractere está presente em uma string.
# O operador not in verifica se um determinado caractere não está presente em uma string.

# 0 1 2 3 4 5 
# p y t h o n
# -5 -4 -3 -2 -1 -0

# nome = 'python'
# print(nome[2])  # t
# print(10 * '-')
# print('t' in nome)  # True
# print('thon' not in nome)  # False

nome = input('Digite seu nome: ')
encontrar = input('Digite um caractere para encontrar no nome: ')

if encontrar in nome:
    print(f'O caractere {encontrar} foi encontrado em {nome}.')
else:
    print(f'O caractere {encontrar} não foi encontrado em{nome}.')