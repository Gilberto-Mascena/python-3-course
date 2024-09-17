# The input function is used to get input from the user, it returns a string
# nome = input('Qual o seu nome? ')
# print(f'Olá {nome}, prazer em te conhecer!')

# The input function can be used to get numbers from the user
# The input function always returns a string, so we need to convert it to a number or float
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
float_1 = float(numero_1)
float_2 = float(numero_2)
soma = float_1 + float_2
print(f'A soma dos números é: {soma:.2f}')   