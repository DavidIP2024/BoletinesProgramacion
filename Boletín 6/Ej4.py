curso = ['matematicas', 'fisica', 'quimica', 'historia', 'lingua']


for asignatura in curso:
    print(asignatura)
    nota_sacache = int(input('Que nota sacache: '))
    if nota_sacache < 5:
        print('tiene que repetir la asignatura ', asignatura)
    elif nota_sacache >= 5:
        print('Asignatura aprobada ', asignatura)
        curso.remove(asignatura)
        print(curso)