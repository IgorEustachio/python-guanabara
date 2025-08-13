#ler um angulo e calcular seu seno, cosseno e tangente

import math

angulo=float(input('digite o seu angulo: '))

seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))

print(f'o angulo de {angulo} tem um seno de {seno:.2f}',end='' f' um cosseno de {cosseno:.2f}, e a tangente de {tangente:.2f}')