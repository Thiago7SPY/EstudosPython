#Calcula a média de 10 números
n = 1
soma = 0
while n <= 10:
    x = int(input('Digite o número %d : ' %n))
    soma = soma + x
    n = n + 1
media = soma / 10
print ('Soma: %d' %media)
