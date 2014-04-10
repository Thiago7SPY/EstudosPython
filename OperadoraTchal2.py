#Calcula o valor de uma conta de telefone.
minutos = int(input('Digite os minutos gastos: '))
if minutos < 200:
    preco = 0.2
else:
    if minutos <= 400:
        preco = 0.18
    else:
        if minutos <= 800:
            preco = 0.15
        else:
            preco = 0.08
print ('Sua Conta de telefone é: '+ str(minutos * preco))