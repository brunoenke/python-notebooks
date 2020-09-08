#Crie um dictionary vazio com o nome Produtos
produtos = dict()
#Adicione 10 produtos a esse dictionary, usando os números de 1 a 10 como chave.
produto = ['Opa Bier 350ml', 1.79]
produto2 = ['Amendoim 500g', 9.79]
produto3 = ['Queijo Parmesão Kg', 16.79]
produto4 = ['Costela Bovina kg', 18.10]
produto5 = ['Café Extraforte 500g', 9.20]
produto6 = ['Macarrão Semola 500g', 3.19]
produto7 = ['Arroz Branco 1kg', 2.99]
produto8 = ['Feijão  1Kg', 4.47 ]
produto9 = ['Filé de Peito de Frango 1kg', 12.27]
produto10 = ['Confeito M&M\'S Chocolate 200g', 12.40]
produtos = {'01':produto,'02':produto2 ,'03':produto3,'04':produto4 ,'05':produto5 ,'06':produto6 ,'07':produto7 ,'08':produto8 ,'09':produto9, '10':produto10}

#Imprima o item com chave 5.
#print (produtos.get('05','item Não encontrado!'))

#Altere o valor do item com chave 9.
produto9 = ['Filé Mignon Suíno kg', 20.15]
produtos['09'] = produto9
#produtos.update({'09':produto9})
print(produtos.get('09'))

#Qual o tamanho do dictionary?
print(len(produtos))

#Adicione um novo produto ao dictionary
produto11 = ['Filé de Tilápia Kg', 9.15]
produtos['11'] = produto11

#Imprima uma lista com todos os valores do dictionary
print(produtos.values())

#Conte o número de ocorrências de cada letra na palavra ‘ANTICONSTITUCIONALISSIMAMENTE’ e imprima na tela. 
palavra = 'ANTICONSTITUCIONALISSIMAMENTE'
dword = dict()
#para cada item = letra  na str palavra:
for letra in palavra:
    #Se a letra não está do dict adiciona letra e incrementa o contador, senão incrementa o contador
    dword[letra] = dword.get(letra,0)+1
print(dword)

#Faça um gráfico de barras para mostrar a distribuição das ocorrências das letras no arquivo LOREM.TXT

#Carregue os itens e seus respectivos preços de um arquivo txt para um Dictionary
#Crie um programa para consultar preços a partir do nome do produto (parcial)
#Crie um programa para fazer um pedido. O usuário deve procurar pelo produto e informar sua quantidade. No fim o programa deve totalizar o pedido e mostrar a lista de produtos comprados, suas quantidades, seus preços e o preço total.
