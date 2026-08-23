print('\033[34m=========desafio 40=========\033[m')
nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
nota3=float(input('Terceira nota: '))
media = (nota1+nota2+nota3)/3
if media <=5:
    print('reprovado voce teve uma media de {:.2f} voce foi REPROVADO'.format(media))
elif media >=6 and media <=7:
    print('voce tirou de media {:>2f}, \033[32mVocê pegou recuperação, Boa sorte!!\033[m'.format(media))
elif media >=7:
    print('voce tirou uma media de {:.2f}, \033[35mPARABENS!! VOCE PASSOU\033[m'.format(media))