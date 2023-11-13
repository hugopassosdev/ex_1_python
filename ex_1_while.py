# Instruções do projeto
# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.
# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

""" numero = 20
while(numero <=20 and numero > 0):
    if (numero == 13):
        continue
    if (numero == 0):
        break
    print(f"Andar {numero}")
    numero = numero - 1 """


numero = 20
while numero > 0:
    if numero != 13:
        print(f"Andar {numero}")
    numero -= 1