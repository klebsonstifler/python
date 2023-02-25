cont = 0
s = 0
while cont < 5:
    n = int(input('Digite um numero inteiro positivo:'))
    if n < 1:
        print('Numero negativo é invalido, digite um numero maior que 0:')
        n = int(input('Digite um numero inteiro positivo:'))
        cont = cont+1
    else:
        cont = cont+1
    s = s + n
else:
    print('A soma dos 5 numeros positivos digitados é ',s)