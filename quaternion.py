from math import sqrt

"""
Implementacion del objeto cuaternion que se define como:
a+bi+cj+dk con a,b,c,d numeros reales
"""
class quaternion:
    def __init__(self,a:float =  0.0, b:float =  0.0, c:float =  0.0, d:float =  0.0) -> None:
        
        # Guardamos las constantes
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    
    """
    Sobrecarga del operador + que permite sumar dos cuaterniones,
    un cuartenio y un entero, o un cuaternion y un real (esta ultima 
    operacion no es conmutativa solo se puede sumar un cuaternion con 
    un entero o un real si estos ultimos estan a la derecha)

    Parametro:
        other: Un cuaternion, un numero entero o un numero real.
    
    Return: devuelve un cuaternion con el resultado de sumarlo con 
            otro cuaternion, un numero entero o un numero real segun sea el caso
    """
    def __add__(self,other):

        if isinstance(other,quaternion):
            return quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d )
        elif isinstance(other,int):
            return quaternion(self.a + float(other), self.b, self.c, self.d)
        elif isinstance(other,float):
            return quaternion(self.a + other, self.b, self.c, self.d)  

    """
    Sobrecarga del operador * que permite multiplicar dos cuaterniones, 
    un cuartenio y un entero o un cuaternion y un numero real 
    (esta ultima operacion no es conmutativa solo se puede multiplicar 
    un cuaternion con un entero o un real si estos ultimos estan a la derecha)

    Parametro:
        other: Un cuaternion, un numero entero o un numero real.
    
    Return: devuelve un cuaternion con el resultado de multiplicarlo con 
            otro cuaternion, un numero entero o un real segun sea el caso
    """
    def __mul__(self,other):

        if isinstance(other,quaternion):
            return quaternion(self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d,
                              self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c,
                              self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b,
                              self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a
                            )
        elif isinstance(other,int):
            return quaternion(self.a * float(other), self.b, self.c, self.d)
        elif isinstance(other,float):
            return quaternion(self.a * other, self.b, self.c, self.d) 
    
    """
    Sobre cargar del operador ~ el cual invierte los signos de los 
    coefecientes de i,j,k 

    Return: Un cuaternion parecido al original donde los coeficiente
            de i,j,k tiene los singos opuesto con respecto al original
    """
    def __invert__(self):
        return quaternion(self.a, -self.b, -self.c, -self.d)

    """
    Sobrecarga del operador -, El cual devuelve la media del cuaternion.
    
    Return: El resultado de calcular la media de los coeficientes del 
            cuaternion

    Nota: Se uso este operador ya que era el unico que esta disponible y 
          no chocaba con las otras sobrecargas 
    """
    def __neg__(self):
        return sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)
    
    """
    Devuelve una representacion del cuaternion como un string

    Return: Un string con una representacion del cuaternion
    """
    def __str__(self):
        return f"{self.a}{self.b:+}i{self.c:+}j{self.d:+}k"

    """
    Permite comparar dos cuaterniones y verificar si son iguales

    Parametros:
        other: Un cuaternion el cual se comparar con el actual cuaternion

    Return: Un valor booleano que indica si los cuaterniones son iguales o no 
    """
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

