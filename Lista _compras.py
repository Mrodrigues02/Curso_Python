def validaEscolha(pergunta, min, max):
  x = int(input(pergunta))
  while((x < min) or (x > max)):
    x = int(input(pergunta))
  return x

def criarArquivo (nomeArquivo):
  try:
      a = open(nomeArquivo, 'wt+')
      a.close()
  except:
    print('Erro na criação do arquivo.')
  else:
    print('Arquivo {} foi criado com sucess!\n'.format(nomeArquivo))

def existeArquivo(nomeArquivo):
  try:
      a = open(nomeArquivo, 'rt')
      a.close()
  except FileNotFoundError:
     return False
  else:
     return True

def cadastrarLista(nomeLista, nomeProduto, quantidade):
  try:
      a = open(nomeLista, 'at')
  except:
    print('Erro ao abrir o arquivo.')
  else:
       a.write('{};{}\n'.format(nomeProduto, quantidade))
  finally:
       a.close()

def listarProdutos(nomeProduto):
  try:
     a = open(nomeProduto, 'rt')
  except:
      print('Erro ao ler o arquivo.')
  else:
      print(a.read())
  finally:
      a.close()

arquivo = 'lista.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo)

while True:
    print('[MENU]')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = validaEscolha('Escolha a opção desejada:', 1, 3)

    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeProduto = input('Nome do produto:')
        quantidade = input('Quantidade:')
        cadastrarLista(arquivo, nomeProduto, quantidade)

    elif op == 2:
        print('Opção de listar arquivo selecionada...')
        listarProdutos(arquivo)
    elif op == 3:
        print('Encerrando programa...')
        break