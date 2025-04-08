import os

def main():
    r1, w1 = os.pipe()  # Pipe para padre -> hijo
    r2, w2 = os.pipe()  # Pipe para hijo -> padre

    pid = os.fork()

    if pid == 0:  # Código del proceso hijo
        os.close(w1)
        os.close(r2)

        r_hijo = os.fdopen(r1, 'r')
        w_hijo = os.fdopen(w2, 'w')

        while True:
            mensaje = r_hijo.readline().strip()
            if not mensaje:
                break
            print(f"Hijo ({os.getpid()}): Recibí del padre -> {mensaje}")

            respuesta = mensaje.upper() + "!!!"
            w_hijo.write(respuesta + "\n")
            w_hijo.flush()  # Asegura que se envíe inmediatamente

        r_hijo.close()
        w_hijo.close()
        os._exit(0)

    else:  # Código del proceso padre
        os.close(r1)
        os.close(w2)

        w_padre = os.fdopen(w1, 'w')
        r_padre = os.fdopen(r2, 'r')

        frases_a_enviar = ["Hola hijo, soy tu padre", "¿Cómo estás hoy?", "Espero que todo bien", "Te envío un saludo"]

        for frase in frases_a_enviar:
            print(f"Padre ({os.getpid()}): Enviando -> {frase}")
            w_padre.write(frase + "\n")
            w_padre.flush()  # Asegura que se envíe inmediatamente

            respuesta = r_padre.readline().strip()
            if respuesta:
                print(f"Padre ({os.getpid()}): Mi hijo me respondió -> {respuesta}")
            else:
                print("Padre: El hijo cerró la conexión o no respondió.")
                break

        w_padre.close()
        r_padre.close()
        os.wait()

if __name__ == "__main__":
    main()