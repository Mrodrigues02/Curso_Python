import random
#Lista de doadores
Participantes = []

#Função para cadastrar os doadores
def cadastra_Participante(nome:str,v_doacao:float):
    Participantes.extend(((nome + ' ') * int(v_doacao // 10)).split())
    return

#Função para sortear os doadores
def sorteia_Participantes():
    random.shuffle(Participantes)
    print(f'Lista de participantes embaralhada: {Participantes}')
    return random.choice(Participantes)

#Dados de entrada
op = int(input('1 - Sim\n2 - Não\nDeseja se cadastrar?'))

#Laço de repetição principal verifica "op"
while op == 1:
    nome = input('Nome do doador:')
    v_doacao = float(input('Quanto deseja doar:'))

#laço de repetição para validar dados de entrada
    while len(nome.strip()) == 0 or v_doacao < 10:
        print('O nome é obrigatório!\nO valor mínimo de doação é R$10')
        nome = input('Nome do doador:')
        v_doacao = float(input('Quanto deseja doar:'))

    cadastra_Participante(nome, v_doacao)

    op = int(input('1 - Sim\n2 - Não\nDeseja se cadastrar?'))
#"if" que verifica a lista e imprime os dados de saída
if len(Participantes) > 0:
   print(f'Lista de doadores: {Participantes}')
   print(f'O ganhador ou a ganhadora foi: {sorteia_Participantes()}')







