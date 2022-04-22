#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep
print('-='*20)
print('Analisando um triangulo')
print('-='*20)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
print('Analisando...')
sleep(1)
if a < b + c and b < a + c and c < a + b: #// codigo da aula
     print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
     print('Os segmentos NÃO PODEM FORMAR!')

# testando se é triangulo // codigo v2
'''if (a + b < c) or (a + c < b) or (b + c < a):
    print('Esse segmento NÃO FORMA um triangulo')
elif (a == b) and (a == c):
    print('Esse segmento é um EQUILATERO.')
elif (a == b) or (a == c) or (b == c):
    print('Esse segmento é um ISÓSCELES.')
else:
    print('Esse segmento é um ESCALENO.')'''
