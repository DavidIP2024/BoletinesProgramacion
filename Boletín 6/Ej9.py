vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

producto_escalar = sum(x*y for x, y in zip(vector1, vector2))

print(producto_escalar)