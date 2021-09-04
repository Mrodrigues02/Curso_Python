ano_nascimento = int(input('Em qual ano você nasceu?'))
ano_atual = int(input('Em que ano estamos?'))
idade = ano_atual - ano_nascimento
nome = input('Qual é o seu nome?')
if idade >= 18:
    print('{},sua entrada foi aprovada.'.format(nome))
