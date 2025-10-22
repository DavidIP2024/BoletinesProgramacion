num1 = float(input("Introduce o primeiro número: "))
num2 = float(input("Introduce o segundo número: "))
suma = num1 + num2
resta = num1 - num2
produto = num1 * num2
if num2 != 0:
    cociente = num1 / num2
    print("O cociente é:", cociente)
else:
    print("Non se pode dividir entre 0.")
    print("A suma é:", suma)
    print("A resta é:", resta)
    print("O produto é:", produto)