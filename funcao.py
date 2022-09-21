"""print() # Imprime uma mensagem
input() # Retorna um dado informado pelo usuário
len() # Recebe uma lista e retorna o tamanho dessa lista
max() # Retorna o maior valor de uma lista"""

# > Criação de Funções

# Função inicial

def saudacao():
    print('Bem-vindo(a)!')
    print('Fique à vontade no meu código horrível.')


saudacao()  # chamando a função

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Bem vindo(a), {nome}')
    print(f'Você está fazendo parte do curso de {curso}')


saudacao('Gabriela', 'Python')

# Função com parâmetro default

def saudacao(nome, curso='Python'):
    print(f'Bem vindo(a), {nome}')
    print(f'Você está fazendo parte do curso de {curso}')

saudacao('Gabriela', 'C++')

# Função com retorno - retorna valor e encerra a função

def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)
print('Resultado: ', resultado)