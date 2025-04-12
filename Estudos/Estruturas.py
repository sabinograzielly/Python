nota1 = eval(input("Digite a 1° nota do aluno:"))
if nota1 < 1 or nota1 > 10:
    print("Erro: A nota 1 deve ser entre 1 e 10")
else:
    nota2 = eval(input("Digite a 2° nota do aluno:"))
    if nota2 < 1 or nota2 > 10:
        print("Erro: A nota 2 deve ser entre 1 e 10")
    else:
        media = (nota1 + nota2) / 2 
        if media >=7:
            print("Você está aprovado! Parabéns!")
        elif media >=5 and media <7:
            print("Você esta de exame.")
        else:
            print("Você foi reprovado!")