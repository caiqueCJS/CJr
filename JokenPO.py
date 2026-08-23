print('\033[35m======Vamos jogar Jokenpo?======\033[m')
import random
opções=('pedra','papel','tesoura')

vitorias = 0
derrotas = 0
empates = 0

while True:

    print('\n====pedra,papel e tesoura======')
    jogador = input('Escolha pedra,papel ou tesoura ').lower().strip()

    #validação da escolha
    if jogador not in opções:
        print('escolha invalida! tente novamente')
        continue

    #escolha da cpu

    cpu = random.choice(opções)

    print('jogador jogou{}'.format(jogador))
    print('cpu jogou{}'.format(cpu))

    #verificação de resultado

    if jogador == cpu:
        print('EMPATE!')
        empates +=1

    elif (jogador == 'pedra' and cpu == 'tesoura') or \
        (jogador == 'papel' and cpu == 'pedra') or \
        (jogador == 'tesoura' and cpu == 'papel'):
        print(f'VOCÊ VENCEU! Eu joguei {cpu}.')
        vitorias +=1

    else:
        print(f'VOCÊ PERDEU! Eu joguei {cpu}.')
        derrotas +=1

    #placar
    print('===placar====')
    print(f'vitorias: {vitorias}')
    print(f'derrotas: {derrotas}')
    print(f'empates: {empates}')

    #jogar novamente

    continuar = input('Quer continuar? [S/N] ').lower().strip()

    if continuar == 'n':
        break

print('=== fim de jogo====')
print(f'vitorias: {vitorias}')
print(f'derrotas: {derrotas}    ')
print(f'empates: {empates}')
print('obrigado por jogar')
