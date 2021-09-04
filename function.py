def borda(s1):
  tam = len(s1)

  if tam:
    print('+','-' * tam,'+')
    print('|',s1,'|')
    print('+','-' * tam,'+')

borda('Olá!')
borda('Lógica de Programação e Algoritimos.')
