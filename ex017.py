#ler o valor do cateto adjecente e do cateto oposto e calcular a hipotenusa

import math

ca=float(input('digite o valor do comprimento do cateto adjecente: '))
co=float(input('digite o valor do comprimento do cateto oposto: '))

print(f'ao somar o cateto adjecente de valor {ca} e o cateto oposto de valor {co}, concluímos que a hipotenusa é {math.sqrt(ca**2 + co**2):.2f}')

