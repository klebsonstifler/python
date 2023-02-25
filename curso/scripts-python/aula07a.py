n1 = int(input('Digite um Valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
ex = n1**n2
res = n1%n2
print('A soma é {}, o produto é {} e a divisao é {:.3f}'.format(s, m, d))
print('Divisão inteira é {}, a potencia é {} e o resto da divisão é {}'.format(di, ex, res))