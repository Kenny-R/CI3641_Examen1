"""
Implementacion del objeto cuaternion que se define como:
a+bi+cj+dk con a,b,c,d numeros reales
"""

from math import sqrt

class quaternion:
    def __init__(self,a:float =  0.0, b:float =  0.0, c:float =  0.0, d:float =  0.0) -> None:
        
        # Guardamos las constantes
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def __add__(self,other):

        if isinstance(other,quaternion):
            return quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d )
        elif isinstance(other,int):
            return quaternion(self.a + float(other), self.b, self.c, self.d)
        elif isinstance(other,float):
            return quaternion(self.a + other, self.b, self.c, self.d)  

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
    
    def __invert__(self):
        return quaternion(self.a, -self.b, -self.c, -self.d)

    def __neg__(self): # Operador de media. Se uso el operador prefijo "-" ya que era el unico disponible que no causaba problemas 
        return sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)
    

    def __str__(self):
        return f"{self.a}{self.b:+}i{self.c:+}j{self.d:+}k"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

