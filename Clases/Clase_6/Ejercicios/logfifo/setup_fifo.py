# setup_fifo.py
import os

fifo_path = 'log_fifo'

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)
    print(f"[Setup] FIFO creado: {fifo_path}")
else:
    print(f"[Setup] FIFO ya existe: {fifo_path}")