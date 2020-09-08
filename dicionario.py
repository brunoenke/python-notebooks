#dictionary é um tipo especial de lista.
#a função DICT() serve para criar um dictionary vazio
dicionario = dict ()
print(dicionario)

#key:value
dicionario = {'chave':'valor'}

lista = ['maçã']
lista.append(True)
lista.append(1000)
lista.append(10.0)

produto = ['Opa Bier 350ml', 1.79]
produto2 = ['Amendoim 500g', 9.79]
produto3 = ['Queijo Parmesão Kg', 16,79]

cupom_fiscal = {'00001':produto}
cupom_fiscal ['00002'] = produto2
cupom_fiscal ['00003'] = produto3

#mostrar a descrição do produto
cupom_fiscal ['00001'][0]
#mostrar o preço do produto
cupom_fiscal ['00001'][1]



#for key, value in cupom_fiscal.items():
#    print('A chave { } está relacionada ao valor { }').format(key,value))

#contar quantas vezes aparece um value (letra)
palavra = 'paralelepipedo'
d = dict()
for letra in palavra:
    d[letra] = d.get(letra,0) + 1
print (d)
