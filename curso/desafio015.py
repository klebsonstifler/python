km = float(input('Quantos km foram percorridos?'))
d = int(input('Quantos dias alugado?'))
vkm = km*0.15
vd = d*60
s = vkm+vd
print('O valor a pagar pela kilometragem rodada é R${}, pelos dias é R${}. O total a pagar é R${}.'.format(vkm,vd,s))