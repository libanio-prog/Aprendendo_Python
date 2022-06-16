
"""
Faça um programa para joga pedra papel e tesoura
"""
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('Suas opções:')
print("""
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")
jogador = (int(input("Qual a sua opção?")))
print('='*20)
print('o computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('='*20)
sleep (1)
print ('JO')
sleep (1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if computador == 0:
    if jogador == 0:
       print('Vocês empataram ')
    elif jogador ==1:
        print ('Você GANHOU ')
    elif jogador == 2:
        print( 'Computador GANHOU ')
    else:
        print( 'Opção inválida escolha de entre 0 e 1 ')

elif computador == 1:
    if jogador == 0:
       print(' Computador ganhou  ')
    elif jogador ==1:
        print ('Vocês empataram ')
    elif jogador == 2:
        print( ' Você ganhou  ')
    else:
        print( 'Opção inválida escolha de entre 0 e 1 ')
elif computador == 2:
    if jogador == 0:
       print('Vocês GANHOU  ')
    elif jogador ==1:
        print ('Computador GANHOU ')
    elif jogador == 2:
        print( ' Vocês empataram')
    else:
        print( 'Opção inválida escolha de entre 0 e 1 ')