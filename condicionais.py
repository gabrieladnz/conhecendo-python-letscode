# > ESTRUTURAS CONDICIONAIS

idade = int(input("Qual a sua idade?"))

if idade >= 18:
    print("Você é maior de idade.")
elif idade <= 10:
    print("Criança.")
else:
    print("Você é menor de idade.")


media = 6
presenca = 70

if media >= 6 and presenca >= 70:
    print('Aprovado!')
else:
    print('Reprovado!')
