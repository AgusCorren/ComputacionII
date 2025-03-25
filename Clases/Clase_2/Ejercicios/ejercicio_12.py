import os
import socket
import time

# Función para manejar la conexión de cada cliente
def manejar_conexion(cliente_socket):
    print(f"El proceso {os.getpid()} está manejando una conexión.")
    mensaje = "Hola, este es un servidor multiproceso.\n"
    cliente_socket.sendall(mensaje.encode())  # Envía un mensaje al cliente
    cliente_socket.close()  # Cierra la conexión después de responder

# Servidor que escucha en un puerto y maneja conexiones con fork()
def servidor():
    host = '127.0.0.1'  # Dirección local
    puerto = 65432       # Puerto en el que el servidor escuchará

    # Crear un socket de servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, puerto))
    servidor_socket.listen(5)  # El servidor puede aceptar hasta 5 conexiones simultáneas

    print(f"Servidor escuchando en {host}:{puerto}...")

    while True:
        # Acepta una nueva conexión
        cliente_socket, cliente_direccion = servidor_socket.accept()
        print(f"Conexión establecida con {cliente_direccion}")

        pid = os.fork()  # Crea un nuevo proceso hijo para manejar la conexión
        if pid == 0:
            # Proceso hijo maneja la conexión
            servidor_socket.close()  # El hijo no necesita el socket del servidor
            manejar_conexion(cliente_socket)
            os._exit(0)  # El hijo termina después de manejar la conexión
        else:
            # Proceso padre continúa esperando nuevas conexiones
            cliente_socket.close()

if __name__ == "__main__":
    servidor()