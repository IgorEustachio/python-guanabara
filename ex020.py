#leia o nome de quatro alunos e mostre a ordem sorteada

import random

a1 = str(input('digite o nome do primeiro aluno: '))
a2 = str(input('digite o nome do segundo aluno: '))
a3 = str(input('digite o nome do terceiro aluno: '))
a4 = str(input('digite o nome do quarto aluno: '))

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)

print(f'a ordem aleatoria é: {alunos}')