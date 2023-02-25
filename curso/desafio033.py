num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
num3 = float(input('Digite mais um numero: '))

maior = 0
menor = 0

if (num1 > num2) and (num1 > num3):
    maior = num1
if (num2 > num1) and (num2 > num3):
    maior = num2
if (num3 > num1) and (num3 > num2):
    maior = num3
if (num1 < num2) and (num1 < num3):
    menor = num1
if (num2 < num1) and (num2 < num3):
    menor = num2
if (num3 < num1) and (num3 < num2):
    menor = num3
print('O maior numero digitado foi {} e o menor foi {}'.format(maior,menor))