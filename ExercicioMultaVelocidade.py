#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7km por km a cima.

vlc = int(input('Digite a velocidade do carro KM/H: '))

if vlc>80:
    print('Você foi multado em R${},00 por estar a {}KM/H'.format((vlc-80)*7, vlc))
else:
    print('Dentro do limite permitido!')