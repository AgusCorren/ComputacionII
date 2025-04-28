# receptor.py
import os

fifo_path = 'chat_fifo'

print("[Receptor] Esperando emisor...")
with open(fifo_path, 'r') as fifo:
    while True:
        mensaje = fifo.readline().strip()
        print(f"[Receptor] Mensaje recibido: {mensaje}")
        if mensaje == "chau":
            break
