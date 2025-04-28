import os

fifo_path = 'mi_fifo'
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

with open('mi_fifo', 'w') as fifo:
    fifo.write("¡Mensaje desde el proceso escritor!\n")