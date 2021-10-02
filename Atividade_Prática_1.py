#Laço de repetição
while True:

#Dados de entrada
    nome_aluno = input('Nome do aluno:')
    nota_final = float(input('Nota final:'))

#Analisando a nota e mostrando a saída
    if (nota_final >= 0) and (nota_final <= 2.9):
        grupo = 'E'
        print('O aluno {} teve nota final de {} e se enquadra no grupo {}.'.format(nome_aluno, nota_final, grupo))

    elif (nota_final >= 3) and (nota_final <= 4.9):
        grupo = 'D'
        print('O aluno {} teve nota final de {} e se enquadra no grupo {}.'.format(nome_aluno, nota_final, grupo))

    elif (nota_final >= 5) and (nota_final <= 6.9):
        grupo = 'C'
        print('O aluno {} teve nota final de {} e se enquadra no grupo {}.'.format(nome_aluno, nota_final, grupo))

    elif (nota_final >= 7) and (nota_final  <= 8.9):
        grupo = 'B'
        print('O aluno {} teve nota final de {} e se enquadra no grupo {}.'.format(nome_aluno, nota_final, grupo))

    elif (nota_final >= 9) and (nota_final <= 10):
        grupo = 'A'
        print('O aluno {} teve nota final de {} e se enquadra no grupo {}.'.format(nome_aluno, nota_final, grupo))

    elif (nota_final < 0) or (nota_final > 10):
        print('Nota inválida!')
        break
#Fim do programa caso a nota seja inválida