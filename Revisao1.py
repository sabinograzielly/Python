numero = input("Digite um número de 5 dígitos:")

if len(numero) != 5 : 
    print("O número deve ter 5 dígitos")
else :
    print("   ".join(numero))