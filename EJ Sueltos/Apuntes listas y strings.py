Lista = [1, 2, 3, 4]
Lista[2] = 'He cambiado esto' #cambiar
Lista.append(8) #añadir
Lista.remove(1) #eliminar por nombre
Lista.pop(posicion) # eliminar por posicion...
print(sorted(Lista)) #Para ordenar alfabeticamente
Listaista.sort(reverse=True) #de mayor a menor
lista.sort() #de menor a mayor
#Usar in cuando se quiera buscar dentro de una lista
#len(objeto) devuelve la cantidad de elementos o caracteres de objeto.
#Lista → cuántos elementos
#String → cuántos caracteres
#print(len(peliculas)) para contar cuantas cosas hay en la lista

texto = "  Hola Pythoneros, bienvenidos al mundo de Python  "

# Eliminar espacios al principio y al final
texto = texto.strip()
print("Sin espacios:", texto)

# Contar cuántas letras tiene (sin contar espacios)
sin_espacios = texto.replace(" ", "")
print("Cantidad de letras:", len(sin_espacios))

# Cambiar todas las letras a mayúsculas
print("En mayúsculas:", texto.upper())

# Cambiar todas las letras a minúsculas
print("En minúsculas:", texto.lower())

# Reemplazar la palabra "Python" por "Java"
nuevo_texto = texto.replace("Python", "Java")
print("Cambiando 'Python' por 'Java':", nuevo_texto)

# Contar cuántas veces aparece la letra "o"
print("Número de 'o':", texto.count("o"))

# Separar las palabras en una lista
lista_palabras = texto.split()
print("Lista de palabras:", lista_palabras)

# Unir las palabras separadas por guiones
texto_unido = "-".join(lista_palabras)
print("Texto unido con guiones:", texto_unido)
