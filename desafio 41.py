print('\033[31m=========desafio 41=========\033[m')
n1=int(input('digite o ano do seu nascimento'))
idade = 2026 - n1
if idade <= 9:
    print('mirim')
elif idade >= 10 and idade <= 14:
    print('infantil')
elif idade >= 15 and idade <= 19:
    print('junior')
elif idade == 20:
    print('senior')
else:
    print('Master')