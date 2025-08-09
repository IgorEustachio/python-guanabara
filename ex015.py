#pergunta os km percorridos e os dias alugados de um carro, calculando total a pagar

km=float(input('quantos km foram percorridos? '))
dia=int(input('quantos dias foi alugado? '))

print(f'voce percorreu {km}km em {dia} dias, com R${(60*dia)+(km*0.15):.2f} a pagar ')