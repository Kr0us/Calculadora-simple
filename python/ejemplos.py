import os

# Obtener la lista de archivos en el directorio actual
current_directory = os.getcwd()
files = os.listdir(current_directory)

print(f"Archivos en el directorio '{current_directory}':")
for file in files:
    print(file)
