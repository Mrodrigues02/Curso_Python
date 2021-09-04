preco = float(input('Qual o preço do produto?'))
desconto = float(input('Qual foi a porcentagem do desconto?'))
print('O valor do produto é {}, o desconto foi de {}% o valor final é {}.'
      .format(preco, desconto, (preco * (desconto / 100))))