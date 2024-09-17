a = 'A'
b = 'B'
c = 1.1

string = 'a = {} b = {} c = {}'
formatacao = string.format(a, b, c)

# formatting with format method
print(formatacao.format(a, b, c))

# formatting with f-string method (:.2f)
string = 'a = {} b = {} c = {:.2f}'
formatacao = string.format(a, b, c)
print(formatacao.format(a, b, c))