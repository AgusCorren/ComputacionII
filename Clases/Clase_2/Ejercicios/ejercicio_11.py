import os
import time

def manejar_solicitud():
    """Simula el manejo de una solicitud de cliente."""
    print(f"El proceso {os.getpid()} está manejando una solicitud.")
    time.sleep(2)  # Simula trabajo del servidor (2 segundos)
    print(f"El proceso {os.getpid()} ha terminado de manejar la solicitud.")

def servidor():
    """Simula un servidor que maneja múltiples clientes (procesos)."""
    for i in range(3):  # Simula 3 solicitudes de clientes
        pid = os.fork()  # Crea un nuevo proceso hijo
        if pid == 0:
            # Proceso hijo
            manejar_solicitud()
            os._exit(0)  # Termina el proceso hijo después de manejar la solicitud
        else:
            # Proceso padre (servidor)
            print(f"El proceso padre (PID {os.getpid()}) ha creado un hijo para manejar la solicitud {i + 1}.")

    # Espera a que todos los hijos terminen
    for _ in range(3):
        os.wait()

if __name__ == "__main__":
    servidor()
