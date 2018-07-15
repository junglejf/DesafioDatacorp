#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// estrutura que representa a árvore , tem ponteiro para os filhos esq e dir, info é o conteúdo armzenado no nó
typedef struct ab{
	int info;
	struct ab *esq, *dir;
}TAB;

// estrutura utilizada pela fila , guarda a informação do conteúdo da árvore
typedef struct NO{
    TAB *info;
    struct NO *prox;
}TNO;

//Fila no estilo FIFO, first in first out, tem ponteiros para ínicio e fim 
typedef struct fila{	
	TNO *ini, *fim;
}TFila;

// inicializa a árvore
TAB *inicializa_TAB(void){
	return NULL;
}

//inicializar a fila
TFila *inicializa(void){
    TFila *f = (TFila*) malloc(sizeof(TFila));
    f -> ini = f-> fim = NULL;
    return f;
}

//checa se a fila está vazia
int vazia(TFila *f){
    return (f-> ini == NULL);
}

// insere o nó da árvore na fila, a inserção sempre ocorre no fim da fila 
TFila * insere(TFila *f, TAB *a){
    TNO *novo = (TNO*) malloc(sizeof(TNO));
    novo->prox = NULL;
    novo->info = a;

    if(vazia(f)){
        f->ini = f->fim = novo;
    }else{
        f -> fim -> prox = novo;
    }
    f -> fim = novo;
 
    return f;
}

// A inserção na Arvoré 
// elementos maiores que o nó sempre são inseridos na direita do nó e menores na esquerda
TAB *insere_TAB(TAB *a, int elem){
	if(!a){
		a = (TAB *) malloc(sizeof(TAB));
		a->info = elem;
		a->esq = a->dir = NULL;
	}
	else if(a->info > elem){
		a->esq = insere_TAB(a->esq,elem);
	}
	else if(a->info < elem){
		a->dir = insere_TAB(a->dir, elem);
	}
	return a;
}

// desalacor a memória que foi alocada para a fila
void libera (TFila *f){
    TNO *p = f-> ini;
    while(p){
        TNO *q = p;
        p = p -> prox;
        free(q);
    }
    free(f);
}

// remove um elemento da fila
TAB *retira (TFila *f){
    if(vazia(f)) exit(1);
    TAB *resp = f->ini->info;
    TNO *p = f->ini;
    f->ini = f->ini->prox;
    if(!f->ini)
            f->fim = NULL;
    free(p);
    return resp;
}

// imprime os elementos que estão na fila
void imprime(TFila *f){
    TFila *aux = inicializa();
    while(!vazia(f)){
        TAB *a = retira(f);
        printf("%d\n",a->info);
        aux = insere(aux,a);
    }
    while(!vazia(aux)){
        f = insere(f , (retira(aux)));
    }
    libera(aux);
}

/* função que imprime em "amplitude"
Inicialmente a raiz da árvoré é alocada na fila
toda vez que um nó é retirado da fila checamos se ele possui filhos
Se sim
Os filhos são inseridos na fila
Dessa forma percorremos a árvore por nível imprimindo os nós a partir da esqueda

Complexidade temporal = O(2n) cada nó é visitado 2 vezes, um para inserir e 1 para retirar = O(n)
Complexidade Espacial também será O(n)

*/
void imprime_largura(TAB *a){
	TFila *f = inicializa();
	insere(f,a);
	while(!vazia(f)){
		TAB *p = retira(f);
		printf("%d ", p->info);
		if(p->esq) insere(f,p->esq);
		if(p->dir) insere(f,p->dir);
	}
	printf("\n");
	libera(f);
}

// imprime a árvore do menor para o maior
void imprime_TAB(TAB *a){ 

	if(!a) return;
	printf("%d ", a->info);
	imprime_TAB(a->esq);
	imprime_TAB(a->dir);
}

// Desaloca memória da árvore binária
void libera_TAB(TAB *a){
	if(!a) return;
	libera_TAB(a->esq);
	libera_TAB(a->dir);
	free(a);
	
}

/*Inicializamos a árvore, preenchemos com valores inteiros e fazemos a busca em largura
*/
int main(){
	TAB *a = inicializa_TAB();
	while(1){
		int n;
		scanf("%d", &n);
		if(n < 0) break;
		a = insere_TAB(a, n);
	}
	imprime_largura(a);
	libera_TAB(a);
	return 0;
}
