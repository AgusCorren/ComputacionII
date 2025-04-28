# emisor_1.py
import os
import time

fifo_path = 'log_fifo'

print("[Emisor 1] Enviando logs...")
with open(fifo_path, 'w') as fifo:
    for i in range(3):
        msg = f"[Emisor 1] Mensaje {i+1}"
        fifo.write(msg + '\n')
        fifo.flush()
        time.sleep(1)

    fifo.flush()
