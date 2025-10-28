# Programa de gestión de acceso a un club deportivo
# - Tupla socios_vip: nombres de socios VIP ("Ana", "Carlos", "Lucía")
# - Lista socios_registrados: almacenar nombres de personas que llegan
# - Bucle que pide nombres hasta que se escriba "fin"
# - Para cada nombre:
#     * Si está vacío → mensaje de advertencia
#     * Si está en socios_vip → mensaje de bienvenida VIP
#     * Si empieza por "A" y no es VIP → mensaje de acceso especial
#     * En cualquier otro caso → mensaje de bienvenida normal
# - Guardar todos los nombres válidos en socios_registrados
# - Al final: mostrar total de socios registrados y lista ordenada alfabéticamente

socios_vip = ('Ana', 'Carlos', 'Lucía')
socios_registrados = []

while True:
    nombre = input("Escribe un nombre (o 'fin' para salir): ")
    if nombre.lower() == "fin":
        break
    if nombre == '':
        print('Debe escribir un nombre')
    elif nombre in socios_vip:
        print('Bienvenid@ VIP', nombre)
        socios_registrados.append(nombre)
    elif nombre.startswith('A'):
        print('Acceso especial por inicial A', nombre)
        socios_registrados.append(nombre)
    else:
        print('Bienvenid@', nombre)
        socios_registrados.append(nombre)

print(sorted(socios_registrados))