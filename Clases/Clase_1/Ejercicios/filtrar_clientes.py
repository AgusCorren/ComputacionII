import argparse
import csv

def filtrar_clientes(args):
    try:
        with open(args.input, 'r', newline='', encoding='utf-8') as infile, open(args.output, 'w', newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row in reader:
                if args.provincia and row['Provincia'] != args.provincia:
                    continue
                if args.edad_min and int(row['Edad']) < args.edad_min:
                    continue
                if args.edad_max and int(row['Edad']) > args.edad_max:
                    continue
                if args.estado_civil and row['EstadoCivil'] != args.estado_civil:
                    continue
                if args.nombre and row['Nombre'] != args.nombre:
                    continue
                if args.apellido and row['Apellido'] != args.apellido:
                    continue
                if args.email and row['Email'] != args.email:
                    continue
                if args.telefono and row['Telefono'] != args.telefono:
                    continue

                writer.writerow(row)

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except ValueError:
        print("Error: Edad debe ser un número entero.")

def main():
    parser = argparse.ArgumentParser(description="Filtra registros de clientes.")
    parser.add_argument('-i', '--input', required=True, help='Archivo de entrada (clientes.txt)')
    parser.add_argument('-o', '--output', required=True, help='Archivo de salida (resultados.txt)')
    parser.add_argument('--nombre', help='Filtrar por nombre')
    parser.add_argument('--apellido', help='Filtrar por apellido')
    parser.add_argument('--provincia', help='Filtrar por provincia')
    parser.add_argument('--edad-min', type=int, help='Filtrar por edad mínima')
    parser.add_argument('--edad-max', type=int, help='Filtrar por edad máxima')
    parser.add_argument('--email', help='Filtrar por email')
    parser.add_argument('--estado-civil', help='Filtrar por estado civil')
    parser.add_argument('--telefono', help='Filtrar por telefono')
    parser.add_argument('--verbose', action='store_true', help='Muestra mensajes adicionales')

    args = parser.parse_args()

    if args.verbose:
        print("Procesando archivo de entrada...")

    filtrar_clientes(args)

    if args.verbose:
        print("Guardando en archivo de salida...")

if __name__ == "__main__":
    main()
