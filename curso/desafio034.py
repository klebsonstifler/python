import math
sal = float(input('Digite o salario do funcionário: R$ '))
if sal <= 1250.0:
    sal = sal + (sal * 0.15)
else:
    sal = sal + (sal * 0.10)

print('Seu novo salário é de R$ {} reias'.format(sal))