import math as m
"""
Clase que almacena informacion de grupos de bloques
Parametros:
    CoordI: El indice donde comienza el grupo de bloques
    CoordF: El indice donde termina el grupo de bloques
    Padre: Direccion de memoria de un grupo de bloques, si 
           este grupo esta contenido en uno mas grande,
           None en caso contrario
    hijoIzq: Direccion de memoria de un grupo de bloques que 
             es la division izquierda del bloque, None en caso
             de no haber sido dividido
    hijoDer: Direccion de memoria de un grupo de bloques que 
             es la division derecha del bloque, None en caso
             de no haber sido dividido
"""
class box:
    def __init__(self,coordI,coordF,padre= None,hijoIzq = None , hijoDer = None) -> None:
        self.coordI = coordI
        self.coordF = coordF
        self.padre = padre
        self.hijoIzq = hijoIzq
        self.hijoDer = hijoDer
    
    """
    Devuleve un string con una representacion del grupo de 
    bloques
    """
    def __str__(self) -> str:
        return f"[{self.coordI},{self.coordF}]"


"""
Clase que implementa el manejador de memoria BuddySystem,
la implementacion esta basada en arboles binarios.

Parametros:
    n: El numero de bloques de memoria a manejar. No siempre es
       igual a la memoria disponible, si n es potencia de 2 
       entonces si son iguales, pero si no, se asignara mas espacio
       del que se utilizara creando una memoria con un tamaño
       potencia de 2 mas grande que n.
"""
class buddySystem:
    
    def __init__(self, n) -> None:
        
        # calculamos la potencia de 2 mas cercana a n

        self.limite = n
        self.disponible = n
        
        self.orden_maximo = m.ceil(m.log2(n))# tomamos el techo log_2(n)
        self.maximo = 2**self.orden_maximo 

        print (f"Se creo una memoria de {self.maximo} bloques y se tendra un limite de uso de {self.limite} bloques")

        self.memoria = [None] * self.maximo
        
        self.espacios_libres = {self.orden_maximo:[box(0,self.maximo - 1)]}

        self.espacios_reservados = {}

    
    """
    Reserva una cantidad indicada de espacio en la memoria y 
    modifica la cantidad de espacio libre disponible repartiendola 
    en bloques de tamaño 2^n

    Parametros:
        nombre: el nombre con el que se relacionara ese espacio en memoria
        cantidad: La cantidad de bloques que se ocuparan y se relacionara
                  con el nombre.
    """
    def reservar_espacio(self,nombre, cantidad):
        if cantidad > self.disponible:
            print("Se sobrepasa el limite")
            return 
        
        if nombre in self.espacios_reservados.keys():
            print(f"Ya existe espacio reservado para '{nombre}'")
            return
        
        orden = -1
        
        for i in self.espacios_libres.keys():
            if 2**i >= cantidad:
                orden = i

        if orden == -1:
            print("No se encontro espacio libre suficiente")
            return
        
        self.asignar_espacio(nombre,cantidad,orden)

        self.disponible -= cantidad
        self.combinar_espacios()
        self.eliminar_listas_vacias() 
    
    
    """
    Busca recursivamente el primer grupo de bloques
    libres que mejor se adapte a la cantidad de bloques
    solicitados.

    parametros:
        nombre: Nombre con el se rellenara los espacios
                en memoria
        cantidad: La cantidad de bloques que se necesita
                  ocupar
        orden: El orden de algun grupo de bloques a comprobar
               para saber si se puede ocupar ese espacio.
    """
    def asignar_espacio(self,nombre,cantidad,orden):

        if 2**(orden-1) < cantidad <= 2**orden:
            contador = 0
            i = self.espacios_libres[orden][0].coordI
            while contador != cantidad:
                self.memoria[i] = nombre
                i += 1
                contador += 1
            self.espacios_reservados[nombre] = (self.espacios_libres[orden].pop(0), orden)

        else:
            bloque_antiguo = self.espacios_libres[orden].pop(0)
            nuevo_orden = orden-1

            nuevo_bloque_1 = box(bloque_antiguo.coordI,bloque_antiguo.coordI+ 2**nuevo_orden - 1,bloque_antiguo)
            nuevo_bloque_2 = box(bloque_antiguo.coordI+2**nuevo_orden, bloque_antiguo.coordF,bloque_antiguo)
            
            bloque_antiguo.hijoIzq = nuevo_bloque_1
            bloque_antiguo.hijoDer = nuevo_bloque_2

            
            if (nuevo_orden not in self.espacios_libres.keys()): self.espacios_libres[nuevo_orden] = []

            self.espacios_libres[nuevo_orden].append(nuevo_bloque_1)
            self.espacios_libres[nuevo_orden].append(nuevo_bloque_2)

            self.asignar_espacio(nombre,cantidad,orden-1)
    
    """
    Dado un nombre libera el espacio en memoria
    relacionado con ese nombre

    Parametro:
        nombre: El nombre asignad al espacio a liberar
    """
    
    def liberar_espacio(self, nombre):
        if nombre not in self.espacios_reservados.keys(): 
            print(f"No hay espacio asignado para '{nombre}'")
            return
        
        intervalo = self.espacios_reservados[nombre][0]
        orden = self.espacios_reservados[nombre][1]

        self.espacios_reservados.pop(nombre)

        for i in range(intervalo.coordI,intervalo.coordF+1): self.memoria[i] = None

        if orden not in self.espacios_libres: self.espacios_libres[orden] = []
        
        self.espacios_libres[orden].append(intervalo)
        self.disponible += 2**orden
        self.combinar_espacios()
    
    """
    Recorre los bloques de espacios vacios y combina estos bloques
    para crear uno mas grande siempre que sea posible (esto se verifica
    si los bloques de espacio son hijos del mismo padre, si esta
    condicion no se cumple no se combinaran los espacios)
    """
    def combinar_espacios(self): 
        orden = 0
        while orden <= self.orden_maximo:
            if orden not in self.espacios_libres.keys(): 
                orden += 1
                continue

            conjunto_de_espacios = self.espacios_libres[orden]

            intervalo_a_agregar = ()
            modificacion = False

            for i in conjunto_de_espacios:
                if i.padre != None and i.padre.hijoIzq in conjunto_de_espacios and i.padre.hijoDer in conjunto_de_espacios:
                    intervalo_a_agregar = i.padre
                    modificacion = True
                    break

            if modificacion == False: 
                orden += 1
            else:
                self.espacios_libres[orden].remove(intervalo_a_agregar.hijoDer)
                self.espacios_libres[orden].remove(intervalo_a_agregar.hijoIzq)

                if orden + 1 not in self.espacios_libres.keys(): self.espacios_libres[orden + 1] = []
                self.espacios_libres[orden + 1].append(intervalo_a_agregar)
       
        self.eliminar_listas_vacias()

    """
    Muestra por pantalla todos los grupos de bloques vacios
    """
    def mostrar_espacios_libres(self):
        for i in self.espacios_libres.keys():           
            print(f"bloques de tamaño {2**i}: ", ", ".join(map(str,self.espacios_libres[i])))
    
    """
    Recorre todas las lista de bloques vacios y si una lista no contiene
    bloques vacios se elimina dicha lista
    """
    def eliminar_listas_vacias(self):
        claves_a_eliminar = []
        for i in self.espacios_libres.keys():
            if self.espacios_libres[i] == []:
                claves_a_eliminar.append(i)
        for i in claves_a_eliminar:
            self.espacios_libres.pop(i)