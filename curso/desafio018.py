import math
angulo = float(input('Digite o ângulo que você deseja:'))
raio = math.radians(angulo)
print('O valor do seno é {:.2f}, cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(raio),math.cos(raio),math.tan(raio)))
