frase = input('Digite uma frase curta:').upper().strip()
print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A primeira vez que letra "A" aparece é na {}ª posição da frase.'.format(frase.find('A')+1))
print('A ultima vez que aparece a letra "A" é na posição {}.'.format(frase.rfind('A')+1))