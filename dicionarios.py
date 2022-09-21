# DICIONÁRIO

# Criando dicionário

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Gabriela','idade': 22, 'altura': 1.73}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos no dicionário

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)