def validaEscolha(pergunta, min, max):
  x = int(input(pergunta))
  while((x < min) or (x > max)):
    x = int(input(pergunta))
  return x

def criarArquivo (nomeVac):
  try:
      a = open(nomeVac, 'wt+')
      a.close()
  except:
    print('Erro na criação do arquivo.')
  else:
    print('Arquivo {} foi criado com sucesso!\n'.format(nomeVac))

def existeArquivo(nomeVac):
  try:
      a = open(nomeVac, 'rt')
      a.close()
  except FileNotFoundError:
     return False
  else:
     return True

def cadastrarLista(nomeCard, nomeVac, lote):
  try:
      a = open(nomeCard, 'at')
  except:
    print('Erro ao abrir o arquivo.')
  else:
       a.write('Nome:{} | Lote:{}\n'.format(nomeVac, lote))
  finally:
       a.close()

def listarProdutos(nomeVac):
  try:
     a = open(nomeVac, 'rt')
  except:
      print('Erro ao ler o arquivo.')
  else:
      print(a.read())
  finally:
      a.close()

arquivo = 'Cartão_de_Vacinação.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo)

while True:
    print('[MENU]')
    print('1 - Cadastrar nova vacina')
    print('2 - Listar vacinas')
    print('3 - Sair')

    op = validaEscolha('Escolha a opção desejada:', 1, 3)

    if op == 1:
        print('Opção de cadastrar nova vacina selecionada...\n')
        nomeProduto = input('Nome da vacina:')
        quantidade = input('Lote:')
        cadastrarLista(arquivo, nomeProduto, quantidade)

    elif op == 2:
        print('Opção de listar arquivo selecionada...')
        listarProdutos(arquivo)
    elif op == 3:
        print('Encerrando programa...')
        break