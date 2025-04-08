import os

while True:
    pid = os.fork()
    if pid == 0:  # Proceso hijo
        print(f"Nuevo proceso creado! PID: {os.getpid()}")
    else:
        print(f"Padre {os.getpid()} creó a {pid}")