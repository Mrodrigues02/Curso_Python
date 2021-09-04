x =  1
while True:
    idade = int(input('Informe a sua iadade:'))
    if idade < 3:
        idade = 0
        print('O valor da sua entrada é : R${}'.format(idade))

    if idade < 11:
        idade = 15
        print('O valor da sua entrada é : R${}'.format(idade))


    if idade >= 12:
        idade = 30
        print('O valor da sua entrada é : R${}'.format(idade))
