import sys


def particao (A, inicio, fim, pivo):
    """ Divide o espaço de modo a colocar todos os elementos
    menores que o pivo antes dele e os maiores depois
    [pivo,p,......,q]
    O partition percorre o vetor com 2 índices p e q e terá complexidade O(n)"""
    p = inicio+1
    q = fim
    pivo_valor = A[pivo]
    pos = pivo
    while(p <= q ):
        while(p < fim+1 and A[p] <= pivo_valor ): # anda com p até achar elemento maior que o pivo
            p += 1
        while(A[q] > pivo_valor): # anda com q até achar elemento igual ou menor que o pivo
            q -= 1
        if(p <= q ): # para fazer a troca e deixar menores,pivo,maiores
            aux = A[p]
            A[p] = A[q]
            A[q] = aux
            p+=1 #incrementar p e q pois os elementos trocados já estão no lado correto da partição
            q-=1
    #posicionar o pivo no local correto x<pivo<y
    aux = A[q]
    A[q] = A[pos]
    A[pos] = aux
    return q

def quick_sort(A, inicio, fim):
    """Utiliza divisão e conquista de forma a ordenar
    recursivamente a parte inferior ao pivo e a parte superior ao pivo com
    o auxílio da função particao
    O pior caso dessa implementação do quicksort será o caso do vetor ordenado"""

    if (inicio >= fim ): #condição de parada da recursão
        return
    pivo = inicio #
    pivo = particao(A, inicio, fim, pivo)
    quick_sort (A, inicio, pivo-1)
    quick_sort (A, pivo+1, fim)


def binary_search(num, vetor, ini, fim):
    """ Função que utiliza divisão e conquista para encontrar um elemento em tempo O(logn), n é o número de elementos da estrutura. É mais eficiente que a busca linear
    , pois a busca binária no pior caso fará logn comparações e a linear n comparações.
    É necessário que o vetor esteja ordenado"""
    pos = int((ini + fim) / 2)
    pivo = vetor[pos]
    #condições de parada
    if (pivo == num): # achar o elemento
        return pos
    elif (ini >= fim): # esgotou o limite de busca
        return False
    elif (pivo < num): # chama para metade superior
        return binary_search(num, vetor, pos + 1, fim);
    elif (pivo > num): # chama para metade inferior
        return binary_search(num, vetor, ini, pos - 1);


def is_sum(soma, vetor):
    """ Função que checa se um dado valor tem um par de elementos distintos cuja soma é igual a ele ( soma = v[i]+v[i+n])?
     Dado um elemento X do vetor(ordenado) o algoritmo faz uma busca binária do complemento dele.
     Aqui o pivo foi escolhido em ordem crescente.
     alvo = soma - pivo
     """
    i = 0  # O(1)
    while (i < len(vetor) - 1): # n+1 comparações , O(n)
        pivo = vetor[i] # O(1)
        alvo = soma - pivo # O(1) , alvo precisa ser diferente do pivo pois v[i] != v[i+n]
        if (alvo != pivo):  # Dispensar busca de elemento duplicado
            if(binary_search(alvo, vetor, i + 1, len(vetor) - 1)):
                return True
        i+=1
    return False

A = [6, 11, 22, 1, 44, 0, 66, 6, 88, 99, 1010]
quick_sort(A,0,len(A)-1)
print(A)
soma = int(sys.stdin.readline())
print(is_sum(soma,A))