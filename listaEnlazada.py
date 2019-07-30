
#-------------------------------------------------------------------------------------------------------------------------
#clase nodo , guardado de datos
class Nodo:


    #metodo contructor
    def __init__(self,nombre=None,siguiente=None):
        self.nombre = nombre
        self.siguiente = siguiente



    # retorna informacion del nodo, sobre-escribiri
    def __str__(self):
        return "%s" %(self.nombre) # %s cantidad de retornos 



#-------------------------------------------------------------------------------------------------------------------------
# clase lista simples
class lSimple:


    # constructor inicializa los atributos
    def __init__(self):
        self.cabeza = None
        self.cola = None # ultima referencia del ultimo nodo



    # metodo agregar
    # recibe objeto tipo nodo (elemento)
    def agregar(self,elemento):
        if self.cabeza == None:
            self.cabeza = elemento # elemento que recibe

        if self.cola != None: # cabeza tiene datos
            self.cola.siguiente = elemento

        self.cola = elemento



    # funcion para mostrar datos
    def listado(self):
        aux = self.cabeza # copia de la cabeza del nodo
        print("*****Datos en la listas*****")
        while aux != None:
            print(aux)
            aux = aux.siguiente



    # metodo eliminar nodo
    def eliminar(self,nombre):
        if self.cabeza.nombre == nombre:
            self.cabeza = self.cabeza.siguiente
            return True
        else:
            aux = self.cabeza
            anterior = aux
            while aux != None:
                if aux.nombre == nombre:
                    anterior.siguiente = nodo.siguiente
                    return True
                anterior = aux
                aux = aux.siguiente
        return False



    # metodo para modficar datos
    # metodo con parametros nombre y nuevo elemento
    def modificar(self,nombre,elemento):
        if self.cabeza.nombre == nombre:
            elemento.siguiente = self.cabeza.siguiente
            self.cabeza = elemento
            return True
        else:
            aux = self.cabeza
            anterior = aux
            while aux != None:
                if aux.nombre == nombre:
                    elemento.siguiente = aux.siguiente
                    anterior.siguiente = elemento
                    return True
                anterior = aux
                aux = aux.siguiente
        return False


#----------------------------------------------------------------------------------------------------------------------------
# metodo main
# metodo principal de arranque de la apliacion
if __name__ == "__main__":

    # inilizacion de  nuetro objeto lista
    ls = lSimple()

    # switch case 
    # impresion de menu
    while(True):
        # menu 
        print("*****Menu*****\n"+
                "1. Agregar dato\n"+
                "2. Mostrar datos\n"+
                "3. Eliminar dato\n"+
                "4. Modificar\n"+
                "5. Salir\n")


        opcion = input("Ingrese una opcion: ")
        # opciones del menu 
        if opcion == "1":
            # crear un nodo para agregar
            nombre = input("Ingrese un nombre: ")
            nodo = Nodo(nombre) # enviando dato al nodo
            ls.agregar(nodo) # agregando nodo a la lista
            print("************\n")

        elif opcion == "2":
            ls.listado()
            print("************\n")
            
        elif opcion == "3":
            dato = input("ingrese nombre del dato a eliminar: ")
            if(ls.eliminar(dato)):
                print("dato fue eliminado de la lista\n")
            else:
                print("el datos no se encuentra dentro de la lista\n")

            print("************\n")

        elif opcion == "4":
            dato = input("ingrese nombre del dato a modificar: ")
            datoNuevo = input("ingrese el nombre nuevo: ")
            nodo = Nodo(datoNuevo)
            ls.modificar(dato,nodo)
            print("************\n")

        elif opcion == "5":
            exit()



