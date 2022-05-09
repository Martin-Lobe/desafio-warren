#funcao recebe um valor, transforma em string para facilmente revertelo, e transforma a string revertida em int.
def reverse(x): 
    a=str(x)
    x=int(a[::-1])
    return x

#valor maximo de 1 milhao
for x in range(10**6):
    #conferir se o numero ou o reverso nao comeca em 0, se a soma deles e impar e se a soma e abaixo de 1 milhao 
    if (x%10!=0) and ((reverse(x)+x)%2==1) and ((reverse(x)+x)<10**6):
        resultado = reverse(x)+x
        #mostrar para o usuario o valor reverisvel
        print(x)

