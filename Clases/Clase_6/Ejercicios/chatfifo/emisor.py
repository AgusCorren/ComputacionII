# emisor.py
import os

fifo_path = 'chat_fifo'

print("[Emisor] Esperando lector...")
with open(fifo_path, 'w') as fifo:
    while True:
        mensaje = input("[Emisor] Ingresá un mensaje: ")
        fifo.write(mensaje + '\n')
        fifo.flush()
        if mensaje == "chau":
            break