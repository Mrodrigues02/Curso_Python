km = float(input('Quantos Km foram rodados?'))
D = int(input('Quantos dias você ficou com o carro?'))
print('Você utilizou o carro por {} dias.\nPercorreu {}Km.\nO total a pagar é R${}'.format(D, km , D * 60 + km * 0.15))