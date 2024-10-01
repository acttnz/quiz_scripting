import os
import sys

def analiza_archivo(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            palabra_contador = 0
            python_contador = 0
            for line in lineas:
                palabras = line.split()
                palabra_contador += len(palabras)
                python_contador += sum(1 for palabra in palabras if palabra.lower() == "python")

            return len(lineas), palabra_contador, python_contador
    except Exception as e:
        print(f"Error leyendo archivo {file_path}: {e}")
        return None

def reporte(directory):
    report_lines = []
    archivo_txt = [f for f in os.listdir(directory) if f.endswith('.txt')]

    if not archivo_txt:
        report_lines.append("No se encontraron archivos de texto.\n")
    else:
        for i in archivo_txt:
            file_path = os.path.join(directory, i)
            result = analiza_archivo(file_path)
            if result:
                lineas, palabra_contador, python_contador = result
                report_lines.append(f"Archivo: {i}\n")
                report_lines.append(f"Número de líneas: {lineas}\n")
                report_lines.append(f"Número total de palabras: {palabra_contador}\n")
                report_lines.append(f"Veces que aparece 'Python': {python_contador}\n")
                report_lines.append("\n")

    with open(os.path.join(directory, "informe.txt"), 'w', encoding='utf-8') as report_file:
        report_file.writelines(report_lines)


if len(sys.argv) != 2:
    print("Uso: python script.py <directorio>")
    sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"Error: {directory} no es un directorio válido.")
    sys.exit(1)

try:
    reporte(directory)
    print(f"Informe generado en {os.path.join(directory, 'informe.txt')}")
except Exception as e:
    print(f"Error durante la generación del informe: {e}")
    sys.exit(1)
