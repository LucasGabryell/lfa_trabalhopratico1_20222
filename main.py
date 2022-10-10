# file read
file = open("arquivo.txt", "r")
txt = file.readlines()
file.close()

deterministico = True

dfa = {}
status = ""
accepting = []
alphabet = []
posicao = 0
subConjuntos = 0

for i in txt:
    # states
    if posicao == 0:
        if i == "#initial\n":
            posicao = posicao + 1
        else:
            dfa[i[0:len(i) - 1]] = {}

    # initial
    elif posicao == 1:
        if i == "#accepting\n":
            posicao = posicao + 1
        else:
            status = i.rstrip('\n')

    # accepting
    elif posicao == 2:
        if i == "#alphabet\n":
            posicao = posicao + 1
        else:
            accepting.append(i.rstrip('\n'))

    # alphabet
    elif posicao == 3:
        if i == "#transitions\n":
            posicao = posicao + 1
        else:
            alphabet.append(i.rstrip('\n'))
