# lista comuns]
lista_vazia = []
numeros = [10,20,30,40]
produtos = ['feijão', 'arroz', 'leite', 'sal', 'farinha']

nova_lista = produtos + numeros # junção das duas linhas
print(nova_lista)

print(len(produtos))
print(sum(numeros))
print(max(numeros))
print(min(numeros))

if 'banana' in produtos:
    print('Tem banana na lista')


for produto in produtos:
    print(produto)

#parte de uma lista
#O ultimo indice do python não aparece
print(produtos[1:3])
print(produtos[1:4])
print(produtos[:4])
print(produtos[:])
