dist = float(input('Digite a distancia da sua viagem em km:'))
val = 0
if (dist <= 200 ):
    val = dist*0.50
    print('O valor da sua viagem será de R$ {} reias'.format(val))
else:
    val = dist*0.45
    print('O valor da sua viagem será de R$ {} reais'.format(val))