import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Procesa archivos de entrada y salida.")

# Agregar argumentos
parser.add_argument('-i', '--input', required=True, help='Archivo de entrada')
parser.add_argument('-o', '--output', required=True, help='Archivo de salida')

# Parsear los argumentos
args = parser.parse_args()

# Usar los argumentos
print(f'Entrada: {args.input}')
print(f'Salida: {args.output}')
