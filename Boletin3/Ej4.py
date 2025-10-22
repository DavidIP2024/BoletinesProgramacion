nome1 = input("Nome da primeira persoa: ")
peso1 = float(input("Peso de " + nome1 + " (kg): "))

nome2 = input("Nome da segunda persoa: ")
peso2 = float(input("Peso de " + nome2 + " (kg): "))

if peso1 >= peso2:
    print(nome1, "pesa máis. Diferenza:", peso1 - peso2, "kg")
else:
    print(nome2, "pesa máis. Diferenza:", peso2 - peso1, "kg")