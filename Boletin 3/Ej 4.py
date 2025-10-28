NombrePersona1 = input('Introduce el nombre de la persona1: ')
NombrePersona2 = input('Introduce el nombre de la persona2: ')
PesoPersona1 = float(input('Introduce el peso de la persona1: '))
PesoPersona2 = float(input('Introduce el peso de la persona2: '))
if PesoPersona1 > PesoPersona2:
    Diferencia = PesoPersona1 - PesoPersona2
    print(NombrePersona1,'pesa',PesoPersona1,"kg")
    print('La diferencia de peso es de:',Diferencia,'kg')
elif PesoPersona2 > PesoPersona1:
    Diferencia = PesoPersona2 - PesoPersona1
    print(NombrePersona2,'pesa',PesoPersona2,'Kg')
    print('La diferencia de peso es de:', Diferencia, 'kg')