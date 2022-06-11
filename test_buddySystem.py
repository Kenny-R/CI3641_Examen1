import buddySystem as bds
a = bds.buddySystem(9)

a.reservar_espacio("a",3)
print(a.memoria)
a.mostrar_espacios_libres()
print()

a.reservar_espacio("b",2)
print(a.memoria)
a.mostrar_espacios_libres()
print()

a.reservar_espacio("c",5)
print(a.memoria)
a.mostrar_espacios_libres()
print()

a.reservar_espacio("d",1)
print(a.memoria)
a.mostrar_espacios_libres()
print()

a.reservar_espacio("e",1)
print(a.memoria)
a.mostrar_espacios_libres()
print()

a.reservar_espacio("f",2)


print(a.memoria)
a.mostrar_espacios_libres()
print()

a.liberar_espacio("d")
a.liberar_espacio("e")
a.liberar_espacio("f")
a.liberar_espacio("b")
a.liberar_espacio("a")

print()

print(a.memoria)
a.mostrar_espacios_libres()