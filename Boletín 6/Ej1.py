curso = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lingua']


for i in range(len(curso)):
    print(curso[i])
    nota = int(input('Que nota sacache: '))
    print('Saquei un', nota, 'en', curso[i])