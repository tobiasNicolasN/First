class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.left = None
        self.right = None

class Arbol:
    def __init__(self,dato):
        self.raiz = Nodo(dato)

    def agregarRecursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.left is None:
                nodo.left = Nodo(dato)
            else:
                self.agregarRecursivo(nodo.left, dato)
        else:
            if nodo.right is None:
                nodo.right = Nodo(dato)
            else:
                self.agregarRecursivo(nodo.right, dato)

    def agregar(self, dato):
        self.agregarRecursivo(self.raiz, dato)

    def preorderRecursivo(self, nodo, lista):
        if nodo is not None:
            lista.append(nodo.dato)
            self.preorderRecursivo(nodo.left, lista)
            self.preorderRecursivo(nodo.right, lista)

    def arbolLista(self):
        lista = []
        self.preorderRecursivo(self.raiz, lista)
        return lista

    def invertirArbolRecursivo(self, nodo):
        if nodo is None:
            return None
        nodo.left, nodo.right = self.invertirArbolRecursivo(nodo.right), self.invertirArbolRecursivo(nodo.left)
        return nodo

    def invertirArbol(self):
        self.raiz = self.invertirArbolRecursivo(self.raiz)

arbolPrueba = Arbol(10)
arbolPrueba.agregar(4)
arbolPrueba.agregar(70)
arbolPrueba.agregar(93)
arbolPrueba.agregar(12)
arbolPrueba.agregar(2)
arbolPrueba.agregar(7)

print(arbolPrueba.arbolLista())
arbolPrueba.invertirArbol()
print(arbolPrueba.arbolLista())
