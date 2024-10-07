# Escritura y lectura de un archivo de texto en Python

# Paso 1: Crear y escribir en el archivo my_notes.txt
with open("my_notes.txt", "w") as file:
    # Escribiendo notas personales en el archivo
    file.write("Nota 1: Recuerda practicar la presentación oral.\n")
    file.write("Nota 2: Revisar las tareas pendientes.\n")
    file.write("Nota 3: Hacer ejercicio regularmente para mantener la salud.\n")

# Paso 2: Leer el contenido del archivo my_notes.txt
with open("my_notes.txt", "r") as file:
    # Leyendo línea por línea
    for line in file:
        # Mostrando cada línea leída en la consola
        print(line.strip())  # strip() elimina espacios en blanco y saltos de línea

# El archivo se cierra automáticamente al salir del bloque 'with'