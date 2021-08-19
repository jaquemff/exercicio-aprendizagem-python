#O programa deverá receber um número desconhecido de valores referentes aos preços das
#mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
#compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro
#que o clinete forneceu, para então calcular e mostrar o valor do troco. Após esta
#operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra
prc_pdt = -999
qnt_pdt = 1
vlr_total = 0

print('Loja Tabajara')

while(prc_pdt != 0):
    prc_pdt = float(input('Produto {}: R$'.format(qnt_pdt)))
    qnt_pdt += 1
    vlr_total += round(prc_pdt, 2)

print('Total R${}'.format(vlr_total))
vlr_rcb = float(input('Dinheiro R$ '))
print('Troco R${}'.format(vlr_rcb-vlr_total))