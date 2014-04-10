#Calcula o valor de uma conta de telefone. 
minutos = int(input('Quantos minutos gastos: '))
if minutos < 200:
    print ('Sua conta de telefone é R$ '+ str(minutos*0.20))
if minutos >= 200 and minutos <= 400:
    print ('Sua conta de telefone é R$ '+ str(minutos*0.18))
if minutos > 400:
    print ('Sua conta de telefone é R$ '+ str(minutos*0.15))    