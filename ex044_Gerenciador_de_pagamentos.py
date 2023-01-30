# simulador de loja com pagamentos.
''' Calcule o preço a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro ou cheque: 10% de desconto.
à vista no cartão: 5% de desconto.
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' CASAS BAHIA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Qual é a opção?'))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 /100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM 20% DE JUROS !!!'.format(totalparcela, parcela))    
else:
    total = preço
    print('Opção inválida!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

