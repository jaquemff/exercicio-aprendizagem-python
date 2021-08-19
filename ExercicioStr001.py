#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Total de letras do primeito nome
# - Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()

print('Nome com maiúsculas: {} '.format(nome.upper()))
print('Nome com minúsculas: {} '.format(nome.lower()))
print('Total de letras sem espaços: {} '.format(len(nome) - nome.count(' ')))
print('Total de letras do primeiro nome: {} '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))