#Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome 'Santo'

cid = str(input('Em que cidade você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')

#Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome

nome = str(input('Digite seu nome completo: ')).strip()

print('silva' in nome.lower())