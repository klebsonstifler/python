nome = input('Digite o nome do funcionario: ')
sal = float(input('Digite o salário atual: R$ '))
nvsal = (sal/100)*15+sal 
print('O funcionário {} obteve 15% de aumento de salário, e o seu novo salário é R$ {} Reias.'.format(nome, nvsal))