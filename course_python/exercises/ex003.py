nome = 'Carlos Eduardo'
altura = 1.83
peso = 77
imc = peso / (altura ** 2)

# O f-string é uma maneira de formatar strings em Python, incluindo variáveis.
print(f'{nome} tem {altura:.2f} de altura, pesa {peso}kg e seu IMC é {imc:.2f}')