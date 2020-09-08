#Leia o arquivo mailbox.txt e crie uma lista chamada Palavras com todas as palavras do arquivo.
arquivo = open('C:\\Users\\Bruno\\Documents\\Programas\\mailbox.txt',"r")
conteudo = arquivo.read()

#Conte o número de palavras que há na lista Palavras.
palavras = conteudo.split()
conta = len(palavras)
print(conta)

#Elimine da lista palavras todos os itens que possuem a palavra “java”.

for palavra in palavras:
    if 'java' in palavras:
        palavras.remove(palavra)
print (palavras)

for item in palavras:
    if item.count('java') > 0 :
        palavras.remove(item)
print (palavras)

#Crie uma nova lista com os primeiros 20 itens da lista Palavras, ordenados em ordem alfabética.
nova_lista = []
for i in range(20):
    nova_lista.append(palavras[i])

nova_lista.sort()
print(nova_lista)

#Crie uma nova lista com os itens da lista Palavras que são um endereço de e-mail.
lista_email = []
for palavra in palavras:
    if palavra.count('@') > 0:
        lista_email.append(palavra)
print(lista_email)