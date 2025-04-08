import os

def main():
    # Crear un pipe
    r1, w1 = os.pipe()  # Pipe para padre -> hijo
    r2, w2 = os.pipe()  # Pipe para hijo -> padre

    pid = os.fork()

    if pid == 0:  # Código del proceso hijo
        os.close(w1)  # Cierra el extremo de escritura del primer pipe
        os.close(r2)  # Cierra el extremo de lectura del segundo pipe

        mensaje = os.read(r1, 100).decode()  # Lee el mensaje del padre
        print(f"Hijo ({os.getpid()}): Recibí del padre -> {mensaje}")

        # Modifica el mensaje y lo envía de vuelta
        respuesta = mensaje.upper() + "!!!"
        os.write(w2, respuesta.encode())

        os.close(r1)
        os.close(w2)
        os._exit(0)

    else:  # Código del proceso padre
        os.close(r1)  # Cierra el extremo de lectura del primer pipe
        os.close(w2)  # Cierra el extremo de escritura del segundo pipe

        mensaje = "Hola hijo, soy tu padre"
        print(f"Padre ({os.getpid()}): Enviando -> {mensaje}")
        os.write(w1, mensaje.encode())  # Envía el mensaje al hijo

        respuesta = os.read(r2, 100).decode()  # Lee la respuesta del hijo
        print(f"Padre ({os.getpid()}): Mi hijo me respondió -> {respuesta}")

        os.close(w1)
        os.close(r2)
        os.wait()  # Espera que el hijo termine

if __name__ == "__main__":
    main()