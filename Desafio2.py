# Escreva uma função que retorne o maior palíndromo de uma string dada. Apenas caracteres [A-Z] são válidos para o palíndromo.
import sys

def cria_matriz(n):
    """ Função para testar a passagem de 2D(i,j) para 1D(k)
    Complexidade  O(n-1*n-1) = O(n^2)"""
    matriz = []
    for i in range (0, n):
        linha = []
        for j in range(0,n):
            if(i!=j):
                linha.append(False)
            else:
                linha.append(True) # se o tamanho de |w| == 1 é palíndrompo, logo a diagonal sempre recebe True
        matriz.append(linha)
    return matriz

def cria_vetor(n):
    """ cria um vetor para expressar a matriz que será usada para guardar os cálculos da tabela n x n
    n é o tamanho da palavra que vai gerar a matriz """
    v = [False] * n * n # o tamanho do vetor será n^2
    for i in range(0,len(v),n+1):
        v[i] = True
    return v

def m2v(i,j,n):
    """Transforma a coordenada de 2D(matriz) para 1D(vetor)
    00 01 02
    10 11 12
    20 21 22
    Exemplo: se n=3 [ordem da matriz quadrada = tamanho da frase]
    T[2][0] ==>> T[x]
    i,j : onde i é coordenada da linha da matriz e j a coordenada da coluna
    n*i + j = índice do vetor
    2*3 + 0 = T[6]
       0  1  2  3  4  5  (6)  7  8
    T[00,01,02,10,11,12,(20),21,22]
    """
    return (n*i + j)

def find_anagrama(frase,v):
    """ Função que dado uma palavra W retorna o maior palíndromo existente em W"""
    tam_frase = len(frase) # O(1)
    if(not tam_frase): #O(1)
        return "" #O(1)
    maior_palindrono = ""+frase[0] #se só tiver 1 letra é palíndromo e não entra no loop
    fim = 0
    inicio = 0
    for i in range(2,tam_frase+1): # até m-2 comparações
        for j in range(0,tam_frase-i+1): # até m - i  comparações, logo O Max(m-2*m-i) = O(m^2)

            if(frase[j]==frase[j+i-1]): #O(1)
                #if(m[j+1][j+i-2] or i==2):
                if(v[m2v(j+1, j+i-2, tam_frase)] or i==2): # O(1)
                    # começamos buscando palíndromos de tamanho 2
                    #Vai comparar A. com N <- FALSE , N. com A <- FALSE, depois i, incrementa e vamos buscar palíndromos de tamanho 3
                    # a única comparação será A. com A  <- TRUE
                    #  |A|N|A|
                    #A.|T|F|T|
                    #N.|F|T|F|
                    #A.|F|F|T|
                    #Maior palíndromo é ANA

                    #m[j][j+i-1] = True
                    v[m2v(j, j+i-1, tam_frase)] = True #O(1)
                #if(m[j][j+i-1] and fim < i):
                if(v[m2v(j, j+i-1, tam_frase)] and fim < i):
                    fim = i # O(1)
                    inicio = j # O(1)
                    maior_palindrono = frase[inicio:inicio+fim] # O(1)
    return maior_palindrono #O(1)


# Main
frase = str(sys.stdin.readline())
frase = frase.replace(" ","") #remove espaço vazio
tamanho_frase = len(frase)
v = cria_vetor(tamanho_frase)

print(find_anagrama(frase,v))






