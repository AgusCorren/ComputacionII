import os

fifo_path = 'fifo_cursor'

print("[Lector] Abriendo FIFO para leer...")
with open(fifo_path, 'r') as fifo:
    mensaje = fifo.read()
    print("[Lector] Mensaje recibido:", mensaje)
