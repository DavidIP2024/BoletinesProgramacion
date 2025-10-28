# Programa para registrar nombres
# - Tupla iniciales_prohibidas: letras que no pueden iniciar un nombre ('X', 'Z')
# - Lista nombres_registrados: almacenar nombres válidos
# - Pedir al usuario cuántos nombres quiere registrar (total_nombres)
# - Bucle for que pide exactamente total_nombres nombres
# - Para cada nombre:
#     * Si está vacío → mensaje de advertencia y no se guarda
#     * Si empieza por letra prohibida → mensaje "Nombre no permitido" y no se guarda
#     * Si es válido → se agrega a la lista y se muestra mensaje "Registrado"
# - Al final: mostrar total de nombres registrados y lista ordenada alfabéticamente

iniciales_prohibidas = ('X','Z')
nombres_registrados = []
total_nombres = int(input('Cuantos nombres deseas registrar?: '))
for i in range(total_nombres):
    nombre = input('Introduce el nombre: ')
    if nombre == '':
        print('Debes escribir un nombre')
    elif nombre.startswith(iniciales_prohibidas):
        print('Nombre no permitido')
    else:
        print('Registrado', nombre)
        nombres_registrados.append(nombre)
print(sorted(nombres_registrados))