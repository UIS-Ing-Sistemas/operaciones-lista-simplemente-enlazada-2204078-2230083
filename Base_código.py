#Por hacer:
#Insertar al final
#Eliminar el primero
#Eliminar el último
#Buscar un elemento por su valor (devuelve Verdadero o Falso)
#Contar elementos de la lista
#Indicar si la lista está vacía
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


Lista1=ListaSE()
Lista1.AgregarInicio(5)
print (Lista1.cabeza.data)
Lista1.AgregarInicio(8)
print (Lista1.cabeza.data)
print (Lista1.cabeza.siguiente.data)
