#x sera o minimo de alunos presentes
#tempoChegada e a lista que armazena os horarios de chegada
tempoChegada = []
x=int(input("Entre limite de alunos: "))
continuar = True
#while e utilizado para receber um numero indeterminado de tempo de chegada, para terminar a tecla "q" deve ser entrda
while (continuar):
    tempo = input("Entre tempo de chegada (q para sair): ")
    if tempo == "q":
        continuar= False
    else:
        tempoChegada.append(int(tempo))

contador_presenca=0
#for e utilizado para verificar se o numero de alunos que chegaram a tempo e maior que x(o minimo)
for aluno in tempoChegada:
    if aluno<=0:
        contador_presenca+=1
    #esse if serve para terminar o for repentinamente uma vez que ja foi conferido que alunos o suficiente chegaram a tempo
    if contador_presenca==x:
        break

#if e else utilizados para informar se a aula sera cancelada ou normal
if contador_presenca==x:
    print("Aula normal")
else:
    print("Aula cancelada")