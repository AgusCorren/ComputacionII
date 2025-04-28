# setup_fifo.py
import os

fifo_path = 'chat_fifo'

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)
    print(f"[Setup] FIFO creado en: {fifo_path}")
else:
    print(f"[Setup] El FIFO ya existe en: {fifo_path}")