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
    # transitions
    else:
        aux = i[i.find(":")+1:i.find(">")]
        if aux in dfa[i[0:i.find(":")]].keys():
            palavra = i[i.find(">")+1:].rstrip('\n')
            if "," in palavra:
                for m in palavra:
                    dfa[i[0:i.find(":")]][i[i.find(":")+1:i.find(">")]].append(m)
            else:
                dfa[i[0:i.find(":")]][i[i.find(":")+1:i.find(">")]].append(palavra)
            deterministico = False
            subConjuntos += 1  
        else:
            palavra = i[i.find(">")+1:].rstrip('\n')
            if "," in palavra:
                dfa[i[0:i.find(":")]][i[i.find(":")+1:i.find(">")]]= palavra.split(",")
                deterministico = False
            else:
                dfa[i[0:i.find(":")]][i[i.find(":")+1:i.find(">")]]=[palavra]
            subConjuntos += 1
