num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
list = [num1,num2,num3]
list.sort()
print('O maior numero é {}'.format(list[2]))
print('O menor numero é {}'.format(list[0]))