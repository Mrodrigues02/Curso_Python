valor = int(input('Digite um valor:'))

if valor >= 100:
    nota_cem = valor // 100
    valor -= nota_cem * 100
    print('notas de 100: {}'.format(nota_cem))

if valor >= 50:
    nota_cinquenta = valor // 50
    valor -= nota_cinquenta * 50
    print('notas de 50: {}'.format(nota_cinquenta))

if valor >= 20:
    nota_vinte = valor // 20
    valor -= nota_vinte * 20
    print('notas de 20: {}'.format(nota_vinte))

if valor >= 10:
    nota_dez = valor // 10
    valor -= nota_dez * 10
    print('notas de 10: {}'.format(nota_dez))

if valor >= 5:
    nota_cinco = valor // 5
    valor -= nota_cinco * 5
    print('notas de 5: {}'.format(nota_cinco))

if valor >= 1:
    nota_um = valor
    print('notas de 1: {}'.format(nota_um))






