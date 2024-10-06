#UNIVERSIDAD ESTATAL AMAZONIC
#TAREA SEMANA 16
#NOMBRE: PAMELA MORALES

# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado 'my_notes.txt'
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Estas son mis notas personales:\n")
    file.write("1. Estudiar física todos los días.\n")
    file.write("2. Practicar programación en Python.\n")
    file.write("3. Leer al menos un libro al mes.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' para leer su contenido
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos en la consola cada línea leída
        print(line.strip())  # strip() se usa para eliminar saltos de línea

# No es necesario cerrar el archivo manualmente debido al uso de 'with'