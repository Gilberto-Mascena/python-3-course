primeiro_valor = (input('Digite o primeiro valor: '))
segundo_valor = (input('Digite o segundo valor: '))

primeiro_valor = float(primeiro_valor)
segundo_valor = float(segundo_valor)

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor :.2f} é maior '
        f'do que {segundo_valor :.2f}')
    
elif primeiro_valor < segundo_valor:
    print(
        f'{primeiro_valor :.2f} é menor '
        f'que {segundo_valor :.2f}')
else:
    print(
        f'{primeiro_valor :.2f} é igual '
        f'a {segundo_valor :.2f}')
