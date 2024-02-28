#Por hacer:
#Insertar al final
#Eliminar el primero
#Eliminar el último
#Buscar un elemento por su valor (devuelve Verdadero o Falso)
#Contar elementos de la lista
#Indicar si la lista está vacía
from operator import truediv
from pickle import TRUE
from tkinter import FALSE
from xmlrpc.client import boolean


class Nodo:
    def __init__(self, valor):
        self.data = valor
        self.siguiente = None
        
class ListaSE:
    def __init__(self):
        self.cabeza = None
        
    def AgregarInicio(self,valor):
        nNodo = Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza = nNodo
            return
        else:
            nNodo.siguiente = self.cabeza
            self.cabeza = nNodo

    def AgregarFinal(self,valor):
        nNodo = valor
        nActual = self.cabeza
        if nActual.siguiente is None:
            nActual.siguiente = nNodo
        else:
            nActual = nActual.siguiente
            
    def EliminarInicio(self):
        if self.cabeza is not None:
            sigTemp = self.cabeza.siguiente
            self.cabeza. #borrar elemento actual(comando por agregar)
            self.cabeza=sigTemp
            
    def EliminarFinal(self):
        nActual = self.cabeza
        buscando = TRUE
        while buscando:
            if nActual.siguiente is None:
                buscando = FALSE
                nActual. #borrar elemento actual(comando por agregar)
            else:
                nActual = nActual.siguiente
            
    def BuscarValor(self,vab):
        nActual = self.cabeza #valor observado
        buscando = TRUE
        while buscando:
            if nActual.valor == vab: #si el nodo observado tiene valor igual al vab
                buscando = FALSE
                return 1 # devolver 1 (verdadero)
            else:
                if nActual.siguiente is None: #si el valor no es igual, se revisa si el nodo apunt a un nodo distinto
                    buscando = FALSE
                    return 0 # si no tiene nodo siguiente, se devuelve 0 (falso)
                else:
                    nActual = nActual.siguiente # si sí tiene nodo siguiente, se observa el próximo nodo
