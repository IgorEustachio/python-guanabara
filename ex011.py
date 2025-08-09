#calcular largura e altura da parece em m, sua area e a quantidade de tinta em l

largura=float(input('digite a largura da parede em metros: '))
altura=float(input('digite a altura da parede em metros: '))
area=largura*altura
print(f'sua parede tem a dimensão de {largura}x{altura} e tem uma area de: {area}m²')
print(f'tinta necessaria em litros: {area/2}')