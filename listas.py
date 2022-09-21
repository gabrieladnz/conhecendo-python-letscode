# > LISTAS

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []      # lista vazia
lista = list()  # lista vazia
lista = [26, 'Gabriela', 3.4444, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [10, 'Gabi', 3.415, True]  # Sempre começa do 0

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])  # indice 0 até o 3
print(lista[3:6])
print(lista[2:6:2])  # Pula de 2 em 2

# Percorrer os elementos da lista com FOR

for elemento in lista:
    print(elemento)

# Utilizando os índices

print('Comprimento da lista', len(lista))

for i in range(len(lista)):
    print(lista[i])

# MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append - adicionando elemento no final da lista

print('Antes do append:', lista)
lista.append(3)

# insert - escolhe elemento/posição que vai colocar o elemento

lista.insert(2, 10)
print('Depois do insert:', lista)

# extend - juntar duas listas

lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend:', lista)

# pop - remover elemento especificado/último

lista.pop()
print('Lista após o pop:', lista)
lista.pop(0)  # especificando elemento que deseja resolver

# remove - elemento que quero remover/ remove o 1º que encontra

lista.remove(3)
print('Depois do remove', lista)

# count# - contas qants vezes um elemento aparece

print('Quantidade de 2 na lista', lista.count(2))

# index - diz o indice de determinado elemento na lista

print('Indice do elemento 12:'), lista.index(12)


# sort - ordenar sua lista

lista.sort()  # ordena de forma crescente
print(lista)

lista.sort(reverse=True)  # ordena de forma decrescente

# ----------> Funções para listas

# Len - quantos elementos têm na lista

print(len(lista))

# Sum - soma todos os elementos da lista

print(sum(lista))

# Max - retorna o maior valor da lista

print('Maior elemento da lista:', max(lista))

# Min - retorna o menor valor da lista

print('Maior elemento da lista:', min(lista))
