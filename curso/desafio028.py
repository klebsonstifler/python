import random
resp = 's'
while (resp == 's'):
    print('Vamos Começar o jogo de Adivinhar')
    num1 = random.randint(1,5)
    num2 = int(input('Qual numero de 1 a 5 o computador escolheu? '))
    if (num2 == num1):
        print('Parabéns você acertou!')
        resp = input('Quer jogar denovo? "S" ou "N"').lower()
    else:
        print('Que pena você errou!')
        print('O numero escolhido foi {}'.format(num1))
        resp = input('Quer jogar denovo? "S" ou "N" ').lower()
print('Fim de Jogo')