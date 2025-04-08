import os
import time

def crear_hijo(tiempo):
    pid = os.fork()
    if pid == 0:  # Código ejecutado por el proceso hijo
        time.sleep(tiempo)
        print(f"Soy un hijo, mi PID es {os.getpid()}", "El PID de mi padre es", os.getppid())
        os._exit(0)  # Salida limpia del hijo

if __name__ == "__main__":
    os.system('clear')
    crear_hijo(2)  # Primer hijo duerme 2s
    crear_hijo(0)  # Segundo hijo duerme 3s

    #time.sleep(1)  # Espera 1 segundo
    #os.wait()  # Espera a que terminen los hijos
    os.waitpid(-1, 0)

    # Mensaje final del padre
    print(f"Soy el padre, mi PID es {os.getpid()}")
    