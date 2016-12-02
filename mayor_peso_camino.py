# Grafo - nodos enlazados -
# Autor: Javier Rivera
# Colaboradores: Liliana Moreno, Arimsay Diaz
# https://repl.it/Ee2n/1

class Nodo:
    def __init__ (self, valor):
        self.info = valor
        self.arcos = []
        
    def enlace (self, ndestino, peso = 1, bdir = False):
        if (type(ndestino) == type(self)):
            arco = Arco(ndestino, peso)
            self.arcos.append(arco)
            if (bdir == True):
                arco = Arco(self, peso)
                ndestino.arcos.append(arco)
            return True
        return False
        
    def muestra_enlaces (self):
        for arco in self.arcos: 
            print arco.nodo.info,
            print arco.peso
            
    def existe_enlace(self, ndestino):
        for arco in self.arcos:
            if (arco.nodo == ndestino):
                return arco
        return False
        
    def eli_enlace (self, ndestino):
        arco = self.existe_enlace(ndestino)
        if (arco != False):
            self.arcos.remove(arco)
            return True
        return False
            
    def __del__(self):
        del self.arcos

        
class Arco:
    def __init__ (self, ndestino, peso=0):
        self.nodo = ndestino
        self.peso = peso

class Grafo:
    def __init__(self, dirigido = True):
        self.__nodos = []
        self.__dirigido = dirigido
        
    def buscaNodo (self, valor):
        for nodo in self.__nodos:
            if (nodo.info == valor):
                return nodo
        return False
    
    def enlace(self, valOrigen, valDestino, peso = 1, bdir = False):
        
        norigen = self.buscaNodo(valOrigen)
        if (not(norigen)):
            return False
            
        ndestino = self.buscaNodo(valDestino)
        if (not(ndestino)):
            return False
        
        if (self.__dirigido == False):
            bdir = True
            
        norigen.enlace(ndestino, peso, bdir)
        return True
        
    def ins_nodo (self, valor):
        if (self.buscaNodo(valor) == False):
            nodo = Nodo(valor)
            self.__nodos.append(nodo)
            return nodo
        return False
        
    def eli_nodo(self, valor):
        nodoE = self.buscaNodo(valor)
        if (nodoE == False):
            return False
            
        for nodo in self.__nodos:
            nodo.eli_enlace(nodoE)
        
        self.__nodos.remove(nodoE)
        return True

def mayor_peso(self,valOrigen, valDestino, visitados =[], elem = '', peso = 0):
        nOrigen = self.buscaNodo(valOrigen)
        nDestino = self.buscaNodo(valDestino)
        if (nOrigen == False or nDestino == False):
            return False

        visitados.append(valOrigen)
	for arco in nOrigen.arcos:
		if arco.peso > peso:
			peso = arco.peso
			elem = arco.nodo.info
		if arco.nodo.info == valDestino:
			print (valOrigen,elem),peso
		if(self.existe_camino(arco.nodo.info, valDestino) and arco.nodo.info not in visitados):
			self.mayor_peso(arco.nodo.info,valDestino,visitados,elem,peso)

    def camino(self,origen,destino,valor = []):
        nOrigen = self.buscaNodo(origen)
	nDestino = self.buscaNodo(destino)
	if (nOrigen.existe_enlace(nDestino) != False):
	    valor.append(True)
	    return True
