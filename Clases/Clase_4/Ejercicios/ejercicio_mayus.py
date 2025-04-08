import os

def main():
    r, w = os.pipe()  # Un solo pipe

    pid = os.fork()

    if pid == 0:  # Código del proceso hijo
        os.close(w)  # El hijo solo lee
        r_hijo = os.fdopen(r, 'r')
        mensaje = r_hijo.readline().strip()
        print(f"Hijo ({os.getpid()}): Recibí -> {mensaje.upper()}")
        r_hijo.close()
        os._exit(0)

    else:  # Código del proceso padre
        os.close(r)  # El padre solo escribe
        w_padre = os.fdopen(w, 'w')
        frase = "Hola hijo"
        w_padre.write(frase + "\n")
        w_padre.close()
        os.wait()

if __name__ == "__main__":
    main()