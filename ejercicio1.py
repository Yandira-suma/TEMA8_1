file = open('archivo.txt', 'w')
file.write('este es el contenido del archivo.\n')
file.close()

file = open('archivo.txt', 'r+')
file.readline()
file.write('añadiendo nuevo contenido.\n')

file.seek(0)
print(file.read())
file.close()
