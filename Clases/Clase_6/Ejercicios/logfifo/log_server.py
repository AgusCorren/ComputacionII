# log_server.py
import os

fifo_path = 'log_fifo'
print("[Log Server] Esperando logs...")

with open(fifo_path, 'r') as fifo:
    while True:
        mensaje = fifo.readline().strip()
        if not mensaje:
            continue
        if mensaje == "fin":
            print("[Log Server] Finalizando servidor.")
            break
        print(f"[Log] {mensaje}")
