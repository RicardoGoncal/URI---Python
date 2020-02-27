# coding: utf - 8


alph = {} # declaração de dicionario sem atribuições
num = 0   # variavel que servirá de inicio para valor de cada chave do dicionario

for ch in range(ord('A'), ord('Z')+1):   # FOR: para cada chave no range de A até Z ( primeiro for referente as chaves do dicionario)
        if ch == ord('A'):               # se a chave for o caracter A logo 'num' recebe o valor 0
            num = 0                      # em caso de a validação for verdadeira
        else:                            # caso não for
            num = num + 1                # o valor da variavel 'num' recebe o incremento

        # cada chave por vez recebe seu valor ( alph[] = representa o dicionario e o que ai dentro dos colchetes são as suas chave, igual como se fosse um indice.
        alph[chr(ch)] = num

n_repeticoes = int(input("Digite o numero de repeticoes: "))  # Pede ao usuario o valor do numero de repeticoes que o laço WHILE vai fazer

x = 0   # inicialização do contador do laço WHILE
while(x < n_repeticoes):                          # realização da condição do laço WHILE

    soma = 0                                      # variavel que atribui o valor da soma das linhas digitadas, de acordo com o exercicio proposto
    lines = int(input("Quantidade de linhas: "))  # pede ao usuario o numero de linhas que corresponde ao numero de frases que serao digitadas
    for lin in range(lines):                      # realização da condição de acordo com o numero de linhas pedidas pelo usuario
        word = input("Digite uma palavra: ")      # para cada linha é pedido uma palavra
        word = word.upper()                       # coloca toda a frase em letras maiusculas
        print(word)                               # apenas confirmação se realmente a frase está maiuscula
        acc = - 1                                 # acumulador para o numero de posicoes da frase
        for w in str(word):                       # laço que percorre cada letra da palavra
                soma = soma + alph[w]             # a variavel soma recebe o valor da chave do dicionario, de acordo com o valor de 'w'
                acc = acc + 1                     # o acumulador recebe o incremento
                soma = soma + acc + lin           # soma recebe o valor do acumulador e do valor da linha do range

    print(soma)                                   # exibi o valor de soma para cada interação do laço for que corresponde as linhas

    x = x + 1                                     # incrementa o valor do contador do laço WHILE