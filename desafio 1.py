nome=input('digite seu nome ')
dia=input('digite o dia do seu nascimento ')
mes=int(input('digite o mes do seu nascimento '))
ano=input('digite o ano do seu nascimento ')
if mes ==1:
    mes='janeiro'
elif mes ==2:
    mes='fevereiro'
elif mes ==3:
    mes='março'
else :
    mes = 'mes invalido'
print('ola', nome , 'voce nasceu no dia', dia, 'do mes de' ,mes, 'de' ,ano)

