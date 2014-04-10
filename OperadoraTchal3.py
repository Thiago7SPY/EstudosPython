#Calcula o valor de uma conta de telefone.
minutos = int(input('Minutos utilizados: '))
if minutos < 200:
    preco = 0.2
elif minutos <= 400:
    preco = 0.18
elif minutos <=800:
    preco = 0.15
else:
    preco = 0.08
    
print ('Conta telefônica: R$%6.2f' % (minutos * preco))