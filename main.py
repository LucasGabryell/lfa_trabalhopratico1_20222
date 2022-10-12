# file read
data = open("dfa.txt", "r")
text = data.readlines()
data.close()

deterministico = True

dfa = {}
status = ""
accepting = []
alphabet = []
step = 0
text.remove('#states\n')
subConjuntos = 0
primeiroState = []

for i in text:
    # states
    if step == 0:
        if i == "#initial\n":
            step = step+1
        else:
            dfa[i[0:len(i)-1]] = {}

    # accepting
    elif step == 1:
        if i == "#accepting\n":
            step = step+1
        else:
            status = i.rstrip('\n')

    # alphabet
    elif step == 2:
        if i == "#alphabet\n":
            step = step+1
        else:
            accepting.append(i.rstrip('\n'))

    # transitions
    elif step == 3:
        if i == "#transitions\n":
            step = step+1
        else:
            alphabet.append(i.rstrip('\n'))

    # transitions
    else:
        aux = i[i.find(":")+1:i.find(">")]
        if aux in dfa[i[0:i.find(":")]].keys():
            word = i[i.find(">")+1:].rstrip('\n')

            if "," in word:
                for m in word:
                    dfa[i[0:i.find(":")]][i[i.find(":")+1:i.find(">")]].append(m)
            else:
                dfa[i[0:i.find(":")]][i[i.find(":")+1:i.find(">")]].append(word)
            deterministico = False
            subConjuntos += 1  
        else:
            word = i[i.find(">")+1:].rstrip('\n')

            if "," in word:
                dfa[i[0:i.find(":")]][i[i.find(":")+1:i.find(">")]]= word.split(",")
                deterministico = False
            else:
                dfa[i[0:i.find(":")]][i[i.find(":")+1:i.find(">")]]=[word]
            subConjuntos += 1

nameState = -1
print(f'entrada: {dfa}')
dfaUpdated ={}
dfaUpdated.update(dfa)
dfaCopy = dfa.copy()
if deterministico == False:
    conjuntoAtual = {}

    for x in range(4): 
        dfaUpdated.update(dfa) 
        for state in list(dfaUpdated):
            for letra in dfa[state]:
                if len(dfa[state][letra]) > 1: 
                    nameState += 1
                    
                    conjuntoAtual = dfa[state][letra] 
                    newState = 'n' + str(nameState) 
                    dfa[state][letra] = [newState]            
                    dfa[newState] = {}  
                      
                    for iguais in dfa:
                        for letras2 in dfa[iguais]:
                            if dfa[iguais][letras2] == conjuntoAtual:
                                dfa[iguais][letras2] = [newState]
                         
                    for finalState in range(len(accepting)): 
                        if accepting[finalState] in conjuntoAtual:
                            accepting.append(newState)   
                    subConjuntos -= 1
                    
                    novoEstado = {} 
                    try:
                        for g in alphabet:
                            for stateIndex in range(len(conjuntoAtual)):
                                if g in dfa[conjuntoAtual[stateIndex]].keys():
                                    if g in novoEstado.keys():
                                        for x in dfa[conjuntoAtual[stateIndex]][g]:
                                            if x not in novoEstado[g]:
                                                a = len(dfa[state][g])

                                                novoEstado[str(g)].append(str(x))

                                                if len(dfa[state][g]) > a:
                                                    dfa[state][g] = [f'{dfa[state][g][0]}'] 
                              
                                    else:
                                        novoEstado[g] = dfa[conjuntoAtual[stateIndex]][g]
                                        
                    except KeyError:
                        print(g, dfa)
                    dfa[newState].update(novoEstado)
                
                    for i in dfa:
                        for j in dfa[i]:
                            if len(dfa[i][j]) > 1:
                                subConjuntos += 1
#print(f'saida: {dfa}')
        
autoType = "dfa"
for i in dfa:
    for j in dfa[i]:
        if len(dfa[i][j]) > 1:
            autoType = "dfa"
            break


 
userInput = input("insira a palavra: ")

erro = False
if autoType == "dfa":
    for i in userInput:
        if i in alphabet:
            status = dfa[status][i][0]
        else:
            erro = True
            break
elif autoType == "nfa":
    pass

if erro:
    print("Palavra invalida")
else:
    if status in accepting:
        print("Palavra aceita")
    else:
        print('Palavra inválida')