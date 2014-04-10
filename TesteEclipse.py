#Calcula o valor da multa... 
v = int ( input('Qual a velocidade de seu carro? '))
if v <= 110:
    print('Está OK!')
if v > 110:
    multa =  (v-110)*5
    print('Sua multa é de '+ str(multa))