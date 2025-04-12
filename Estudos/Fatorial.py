numero = input('Digite um número inteiro: ')
numero = eval(numero)
fatorial=numero 
while numero >= 2:
    fatorial = fatorial * (numero - 1)
    numero -= 1 #numero = numero - 1 
print (fatorial)
