from multiprocessing import Process, Queue, Pipe
import time
import random

def sucursal(conn):
    pedidos = ["Pizza", "Lomito", "Empanadas"]
    for i in range(5):
        pedido = random.choice(pedidos)
        print(f"[Sucursal] Enviando pedido: {pedido}")
        conn.send(pedido)
        time.sleep(1)
    conn.send("FIN")
    conn.close()

def intermediario(conn, cola):
    while True:
        pedido = conn.recv()
        if pedido == "FIN":
            print("[Intermediario] Señal de fin recibida. Cerrando.")
            for _ in range(2):
                cola.put("FIN")
            break
        print(f"[Intermediario] Recibido por pipe: {pedido}, enviado a cola")
        cola.put(pedido)

def cocinero(nombre, cola):
    while True:
        pedido = cola.get()
        if pedido == "FIN":
            print(f"[{nombre}] Cerrando cocina.")
            break
        print(f"[{nombre}] Cocinando: {pedido}")
        time.sleep(random.uniform(1, 2))
        print(f"[{nombre}] {pedido} listo!")

if __name__ == "__main__":
    cola_pedidos = Queue()
    parent_conn, child_conn = Pipe()

    p_sucursal = Process(target=sucursal, args=(child_conn,))
    p_intermediario = Process(target=intermediario, args=(parent_conn, cola_pedidos))
    cocineros = [Process(target=cocinero, args=(f"Cocinero-{i+1}", cola_pedidos)) for i in range(2)]

    p_sucursal.start()
    p_intermediario.start()
    for c in cocineros: c.start()

    p_sucursal.join()
    p_intermediario.join()
    for c in cocineros: c.join()
