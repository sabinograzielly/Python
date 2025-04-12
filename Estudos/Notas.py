nota1 = input("Digite a 1° Nota do Aluno:")
nota1 = eval (nota1) # transforma em float 
peso1 = input("Digite o peso da 1° nota:")
peso11 = eval (peso1)
nota2 = input("Digite a 2° Nota do Aluno:")
nota2 = eval (nota2)
peso2 = input("Digite o peso da 2° nota:")
peso2 = eval (peso2)

if int(peso1) + int(peso2) >10:
    print("A soma dos pesos não pode ser maior que 10!")
    exit(0)
else:
    media = (int(nota1) * int(peso1) + int(nota2) * int(peso2)) / (int(peso1) + int(peso2))
    print(f'A média do aluno é {media}') #   com a chave o valor da média é impresso no terminal 