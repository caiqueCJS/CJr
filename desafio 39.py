print('\033[35m==========desafio 39===========\033[m')
ano=int(input('digite o ano do seu nascimento:'))
idade = 2026-ano
if idade == 18:
    print('voce ja tem que estar alistado')
elif idade >=16 and idade <18:
    n1= 18-idade
    print ('esta na hora de voce se alistar falta \033[36m{}\033[m'.format(n1))
elif idade >=0 and idade <16:
    print('voce ainda não deve se alistar')
else:
    n1=18-idade
    print('Voce ja passou {} anos do prazo de alistamento'.format(n1))