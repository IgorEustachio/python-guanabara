#calcula o salario e a % de aumento de um funcionario, mostrando seu novo salario

salario=float(input('digite seu salario em R$: '))
aumento=int(input('digite o aumento em %: '))

salariofinal=salario+(salario*aumento/100)

print(f'o seu salario de R${salario:.2f}, com {aumento}% de aumento, foi para R${salariofinal:.2f}')