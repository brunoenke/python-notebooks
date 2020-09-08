#Escreva um programa pedindo para o usuário digitar 5 números, 
# armazene cada número digitado pelo usuário em uma lista, imprima o maior e o menor número.
 
numeros = []
for n in range(5):
    numeros.append(input('Digite um número '))
print(numeros)
print(max(n))
print(min(n))