#leia um nome e mostre o nome com todas as letras maiusculas e minusculas, letras no total e no primeiro nome

nome=str(input('digite seu nome completo: '))

print(f'nome com todas as letras maiusculas: {nome.upper()}')
print(f'nome com todas as letras minusculas: {nome.lower()}')
print(len(nome))
print(len(nome.split()[0]))
