# coding: utf - 8

# Exercicio String #

# Informe o numero de testes #
n_testes = int(input())

# While com as condicões #

for i in range(n_testes):
    raj,shel = input().split()

    if (raj == shel):
        print('empate')
    else:
        if (raj == 'tesoura' and (shel == 'papel' or shel == 'lagarto')):
            print('rajesh')
        elif (raj == 'papel' and (shel == 'pedra' or shel == 'spock')):
            print('rajesh')
        elif (raj == 'pedra' and (shel == 'lagarto' or shel == 'tesoura')):
            print('rajesh')
        elif (raj == 'lagarto' and (shel == 'spock' or shel == 'papel')):
            print('rajesh')
        elif (raj == 'spock' and (shel == 'tesoura' or shel == 'pedra')):
            print('rajesh')
        else:
            print('sheldon')

    
