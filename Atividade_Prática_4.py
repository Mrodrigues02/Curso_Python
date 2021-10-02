#Lista que recebe os produtos
x = []
#Cadastra um novo produto
def adc_Produto(produto_para_cadastrar: dict):
    x.append(produto_para_cadastrar)
    return
#Dados de entrada
op = int(input('1 - Sim\n2 - Não\nDeseja cadastrar um produto?'))
while op == 1:
    novo_produto = {}
    novo_produto['codigo'] = int(input('Digite o código do produto: '))

#Validação do código do pruduto
    if novo_produto['codigo'] == 0:
        print('Código de produto inválido, encerrando programa...')
        break

    novo_produto['estoque'] = int(input('Quantidade no estoque: '))
    novo_produto['minimo'] = int(input('Quantidade minima do estoque: '))

    adc_Produto(novo_produto)
op = int(input('1 - Sim\n2 - Não\nDeseja cadastrar um produto?'))

#Dados de saída
if len(x) > 0:
    print('Lista de produtos pelo código em ordem crescente:')
    print("Código".center(10), end='')
    print("Estoque".center(10), end='')
    print("Mínimo".center(10))

#Lista ordenada
    for produto in sorted(x, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))
else:
    print('Não há nada na lista.')

