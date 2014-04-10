a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a > b and a > c:
    print ('O número %d é maior' %a)
if b > a and b > c:
    print ('O número %d é maior' %b)
if c > a and c > b:
    print ('O número %d é maior' %c)
else:
    print('Os três números são iguais!')  