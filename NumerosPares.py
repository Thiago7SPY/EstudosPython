#Imprime os números pares entre 0 e um número fornecido pelo user
num = int(input('Digite um número: '))
x = 0

while x < num:
    x=x+1
    if x % 2 == 0:
        print (x) 