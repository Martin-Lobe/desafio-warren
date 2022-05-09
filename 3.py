from itertools import combinations

vetor = []
n=int(input("Entre o numero n: "))
continuar = True
while (continuar):
    elemento = input("Entre elemento do vetor (q para sair): ")
    if elemento == "q":
        continuar= False
    else:
        vetor.append(int(elemento))
vetor.sort()
#pegar lista da sandy
#procurar quando diferenca e 0 e aumentar
#procurar para combinacoes com intertools que comecam em 1 e aumentam

possibilidades = []
possi = []
for elemento in vetor:
    while (sum(possi)+elemento) <= n:
        possi.append(elemento)
    if elemento == vetor[1]:
        maximo = len(possi)
    possibilidades = possibilidades + possi
    possi=[]

def achar_combinacao(possibilidades,maximo):
    badongas = [0,1,-1,2,3,-3]
    resultados = []
    comb = []
    for diferenca in badongas:
        for tamanho in range(1,maximo):
            comb = list(combinations(possibilidades,tamanho))
            print(comb)
            for i in comb:
                if sum(i)==(n+diferenca):
                    resultados.append(i)
            if resultados != []:
                return resultados
        
print(achar_combinacao(possibilidades,maximo))
'''
vetor.sort(reverse=True)
listas_boas = []
lista = []
while sum(lista) < n:
    for elemento in vetor:
        if(n-sum(lista))%elemento==0:
            lista.append(elemento)
print(lista)


somas = []
soma = []
possibilidades = []
continuar = True
possi = []
for elemento in vetor:
    while (sum(possi)+elemento) <= n:
        possi.append(elemento)
    possibilidades.append(possi)
    possi=[]

print(possibilidades)

possiveis = []
soma=0
for i in range(len(possibilidades)):
    listaEscolhida = possibilidades[i]
    jlista = []
    for j in listaEscolhida:
        jlista.append(j)
        for k in possibilidades:
            klista = []
            soma=0
            for l in k:
                klista.append(l)
                soma = sum(jlista)+sum(klista)
                if soma>=n:
                    break;
            if soma==n:
                print(soma)
                print(klista)
                print(jlista)
                print('---------------------------')
                possiveis.append(klista+jlista)


print(possiveis)

# while continuar:
#     atual=1
#     while sum(soma)<n:
#         soma.append(vetor[atual])
#     while sum(soma)!=
'''


