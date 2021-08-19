#Faça um programa que mostre na tela uma contagem regressiva para o estou de fogos
#de artifício, indo de 10 até 0, com uma pauda de 1 segundo entre eles.

from time import sleep

print('A CONTAGEM REGRESSIVA IRÁ COMEÇAR!')
sleep(2)
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('FIM!')