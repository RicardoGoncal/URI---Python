# -*- coding: utf-8 -*-

# Cifra de Cesar

# geração de alfabeto via dicionario
def cria_alpha():
    alpha = {}

    i = 0
    for letra in range(ord('A'), ord('Z')+1):
        alpha[i] = chr(letra)
        i = i + 1

    return alpha  

# chamada da função main
if __name__ == '__main__':

    al = cria_alpha()  # invoca a funcao cria alfabeto e atribui a variavel
    n_teste = int(input('digite o numero de casos de teste: '))   # solicita numero de testes

    for n in range(n_teste):                                  # laço para os casos de teste
        palavra = input('digite a palavra a ser alterada: ')  # pede a palavra que vai ser alterada
        palavra = palavra.upper()                             # coloca a palavra toda em maiuscula
        desloc = int(input('digite o numero de deslocamento: '))  # pede o numero de deslocamentos
        nova = ''    # inicializacao da variavel de texto

        for letra in palavra:            # laço para percorrer toda palavra
            alt = 0                      # inicia variavel para troca(indice - deslocamento)
            n_alt = 0                    # inicia variavel para armazenar alteração se a anterior for negativa
            for i in al:                # laço que percorre o dicionario criado
                if letra == al[i]:      # verifica se a letra da palavra é igual a do dicionario
                    alt = i - desloc    # variavel recebe indice do dicionario - deslocamento pedido

                    if alt < 0:
                        n_alt = 26 - (alt * -1)  # novo indice de troca é atribuido
                        letra = al[n_alt]        # letra atribui a letra do indice indicado
                        nova = nova + letra      # incremento e concatenação da nova palavra
                        break                    # break caso a letra seja encontrada e trocada
                    else:
                        n_alt = alt              # else executa o contrario da parte de cima
                        letra = al[n_alt]
                        nova = nova + letra
                        break
            
        print(nova)            # exibe cada palavra nova de acordo com o numero de testes pedidos
                



            
            

                      
        
            






    


