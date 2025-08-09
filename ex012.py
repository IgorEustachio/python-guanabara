#calcula o preço e o desconto de um produto e mostra seu novo preço

preco=float(input('digite o preço do produto em R$: '))
desconto=int(input('digite o desconto em %: '))

precofinal=preco-(preco*desconto/100)

print(f'o preço final do seu produto de valor {preco} com desconto de {desconto}% é {precofinal:.2f}R$')