import os

def main():
    read_fd, write_fd = os.pipe()  # Creamos el pipe

    pid = os.fork()  # Creamos el hijo

    if pid == 0:
        # Proceso hijo
        os.close(write_fd)  # No necesita escribir
        r = os.fdopen(read_fd)  # Convertimos el fd en objeto tipo archivo
        mensaje = r.read()
        print(f"[Hijo] Mensaje recibido: {mensaje}")
        r.close()
    else:
        # Proceso padre
        os.close(read_fd)  # No necesita leer
        w = os.fdopen(write_fd, 'w')  # Lo abrimos como archivo para escritura
        w.write("Hola desde el padre!\n")
        w.close()

if __name__ == '__main__':
    main()
