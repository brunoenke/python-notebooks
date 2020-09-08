#Quais letras do alfabeto não aparecem no arquivo “lorem.txt”?
arquivo = open("lorem.txt", 'r')
# ler o arquivo
conteudo = arquivo.read()

#importar contantes do alfabeto
from string import ascii_uppercase, ascii_lowercase, ascii_letters

for char in ascii_letters:
    #contar
    contador = conteudo.count(char)
    if (contador == 0):
        print('A letra {} não está no arquivo lorem.txt'.format(char))