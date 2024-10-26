"""
Operator lógico AND
and - todos os valores precisam ser verdadeiros
Se qualquer valor for falso, o resultado será falso
São considerados falsos: False, 0, 0.0, '', [], (), {}, None
"""

entrada = input('[E]ntrar ou [S]air: ')

senha_digitada = input('Digite a senha: ')
senha_permitida = '123456'

# Só entra no if se a exprsssão avadaliada for verdadeira ou seja, se a entrada for 'E' e a senha for igual a senha permitida
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Bem-vindo!')
else:
    print('Até logo!')  