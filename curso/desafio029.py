vel = float(input('Digite a velocidade do veiculo: '))
mul = 0
if (vel > 80):
    mul = (vel - 80) * 7
    print('Você foi multado porque estava acima de 80 km/h')
    print('É cobrado R$7,00 a cada km acima da velocidade.')
    print('você deverá pagar uma multa de R$ {} reais'.format(mul))
else:
    print('Você estava dentro da velocidade permitida que é 80 km/h.')