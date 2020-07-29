def exibe_status(n_aluno, f_aluno):
    if n_aluno >= 5.0 and f_aluno <= 25:
        if n_aluno >= 7.0:
            print('Aluno aprovado!')
        else:
            print('Aluno em recuperação!')
    else:
        print('Aluno reprovado!')
    return

nota = float(input('Insira a sua nota: '))
presenca = int(input('Insira a sua quantidade de faltas: '))

exibe_status(nota, presenca)