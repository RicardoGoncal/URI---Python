# -*- coding: utf-8 -*-

# Exercicio que combina as strings digitadas


# Inicialização do bloco Main
if __name__=='__main__':

    n_testes = int(input('digite o numero de testes: '))   # Solicita o numero de testes

    for n in range(0, n_testes):                         # laço que faz as iterações de numeros de testes
        string1 = input('digite a primeira String: ')    # pede ppalavra 1
        string2 = input('digite a segunda String: ')     # pede palavra 2
        nova = ''                                        # variavel que ira armazenar a palavra final
        if len(string1) > len(string2):
            maior = string1
            menor = string2
        else:                                           # comparação simples de qual String é maior
            maior = string2
            menor = string1

        volta = 0                                       # atribui 0 a variavel
        while(volta < len(maior)):                      # enquanto volta for menor que a maior palavra
            
            if volta < len(menor):
                nova = nova + string1[volta] + string2[volta] # essa comparação é realizada em etapas
            elif volta >= len(string1):                       # enquanto volta for menor que a menor palavra
               nova = nova + string2[volta]                   # pega-se as letras em ordem de cada palavra
            elif volta >= len(string2):                       # caso volta ultrapsse o valor estipulado no primeiro IF
                nova = nova + string1[volta]                  # a palavra é completada de acordo com uma das 2 situações seguintes
                
            volta += 1                                        # incrementa 1 em volta 
        print(nova)                                           # exibe a palavra formatada