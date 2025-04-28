import os
import time

fifo_path = 'fifo_cursor'

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

print("[Escritor] Abriendo FIFO para escribir...")
with open(fifo_path, 'w') as fifo:
    print("[Escritor] Enviando mensaje...")
    fifo.write("Mensaje mágico desde el escritor.\n")
    fifo.flush()
    print("[Escritor] Mensaje enviado.")
