#função que concatena a 1ª letra do nome, o sobrenome e os 2 ultimos digitos do RU
def criar_email():
#Dados de entrada
   nome = input('Digite o seu nome:')
   Snome = input('Digite o seu sobrenome:')
   Ru = str(input('Digite o seu RU:'))
   conc = nome[0] + Snome + Ru[-2:]
#Dados de saída
   print('Sr.{} {}, seu email é {}@algoritimos.com.br'.format(nome, Snome, conc))
#Chamada da função
criar_email()


#3763432