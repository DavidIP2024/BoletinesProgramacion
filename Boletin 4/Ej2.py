print("1... Cadrado")
print("2... Triangulo")
print("3... Círculo")

opcion = input("Elixe unha opción: ")

if opcion == "1":
    lado = float(input("Introduce o lado do cadrado: "))
    print("A superficie do cadrado é:", lado * lado)
elif opcion == "2":
    base = float(input("Introduce a base do triángulo: "))
    altura = float(input("Introduce a altura do triángulo: "))
    print("A superficie do triángulo é:", (base * altura) / 2)
elif opcion == "3":
    radio = float(input("Introduce o radio do círculo: "))
    print("A superficie do círculo é:", 3.14 * radio * radio)
else:
    print("Opción incorrecta")