#import buddySystem as bds
import buddySystemMK2 as bds2

b = bds2.buddySystem(8)

b.reservar_espacio("a",1)
b.reservar_espacio("b",1)
b.reservar_espacio("c",1)
b.reservar_espacio("d",1)
b.reservar_espacio("e",1)
b.reservar_espacio("f",1)
b.reservar_espacio("g",1)
b.reservar_espacio("h",1)

print(b.memoria)
b.mostrar_espacios_libres()
print()

b.liberar_espacio("d")
b.liberar_espacio("e")

print(b.memoria)
b.mostrar_espacios_libres()
print()


""" b.reservar_espacio("a",3)
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.reservar_espacio("b",2)
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.reservar_espacio("d",1)
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.reservar_espacio("e",1)
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.reservar_espacio("f",2)
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.liberar_espacio("d")
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.liberar_espacio("e")
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.liberar_espacio("f")
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.liberar_espacio("b")
print(b.memoria)
b.mostrar_espacios_libres()
print()

b.liberar_espacio("a")
print(b.memoria)
b.mostrar_espacios_libres()
print()


""" """ a = bds.buddySystem(9)

a.reservar_espacio("a",3)
print(a.memoria)
print(a.espacios_libres)
print(a.espacios_reservados)
print()

a.reservar_espacio("b",2)
print(a.memoria)
print(a.espacios_libres)
print(a.espacios_reservados)
print()

a.reservar_espacio("c",5)
print(a.memoria)
print(a.espacios_libres)
print(a.espacios_reservados)
print()

a.reservar_espacio("d",1)
print(a.memoria)
print(a.espacios_libres)
print(a.espacios_reservados)
print()

a.reservar_espacio("e",1)
print(a.memoria)
print(a.espacios_libres)
print(a.espacios_reservados)
print()

a.reservar_espacio("f",2)


print(a.memoria)
print(a.espacios_libres)
print(a.espacios_reservados)
print()

a.liberar_espacio("d")
a.liberar_espacio("e")
a.liberar_espacio("f")
a.liberar_espacio("b")
a.liberar_espacio("a")

print()

print(a.memoria)
print(a.espacios_libres)
print(a.espacios_reservados)
 """

