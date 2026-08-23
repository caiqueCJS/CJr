print('\033[33m====== DESAFIO 38 ======\033[m')
print('digite o valor de 2 numeros inteiros')
n1=int(input('primeiro numero: '))
n2=int(input('segundo numero: '))
if n1 >n2:
    print (' o primeiro valor {} é maior'.format(n1))
elif n2>n1:
    print('o segundo valor \033[33m{}\033[m é maior'.format(n2))
else:
    print('os valores são iguais')
