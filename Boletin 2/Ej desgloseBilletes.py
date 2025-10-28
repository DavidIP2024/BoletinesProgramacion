CantidadDinero = int(input("Introduce la cantidad de dinero que desea desglosar: "))

Billete100 = CantidadDinero // 100
CantidadDinero = CantidadDinero % 100

Billete20 = CantidadDinero // 20
CantidadDinero = CantidadDinero % 20

Billete5 = CantidadDinero // 5
CantidadDinero = CantidadDinero % 5

Moneda1 = CantidadDinero

print("Desglose:")
print("Billetes de 100€:", Billete100)
print("Billetes de 20€:", Billete20)
print("Billetes de 5€:", Billete5)
print("Monedas de 1€:", Moneda1)