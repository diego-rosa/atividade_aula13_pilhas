from Livro import Livro

class Pilha:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self,titulo,autor):
        livro = Livro(titulo,autor)
        if self.inicio == None:
            self.inicio = livro
            self.fim = livro 
        else:
            self.fim.proximo = livro
            self.fim = livro
        self.imprimir()
    
    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia!\n--------------")
        else:
            print("---------------------\n")
            texto = ""
            aux = self.inicio
            while( aux ):
                texto += aux.titulo + " - "
                aux = aux.proximo
            print(texto)

    def remover(self):
        if self.inicio == None:
                print("Lista Vazia!\n--------------")
        else:
            if self.inicio.proximo == None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.fim.proximo
            self.imprimir()
'''
from No import No

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self,valor):
        no = No(valor)
        if self.inicio == None:
            self.inicio = no
            self.fim = no 
        else:
            self.fim.proximo = no
            self.fim = no
        self.imprimir()
    
    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia!\n--------------")
        else:
            print("---------------------\n")
            texto = ""
            aux = self.inicio
            while( aux ):
                texto += aux.dado + " - "
                aux = aux.proximo
            print(texto)

    def remover(self):
        if self.inicio == None:
                print("Lista Vazia!\n--------------")
        else:
            if self.inicio.proximo == None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.inicio.proximo
            self.imprimir()
'''