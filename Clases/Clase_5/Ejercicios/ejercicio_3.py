from multiprocessing import Process, Queue, Manager
import time
import random

def productor(nombre, cola):
    pedidos = ["Empanadas", "Pizza", "Milanesa", "Hamburguesa", "Lomito"]
    for _ in range(3):
        pedido = f"{random.choice(pedidos)} ({nombre})"
        print(f"[{nombre}] Pedido recibido: {pedido}")
        cola.put(pedido)
        time.sleep(random.uniform(0.2, 1))

def consumidor(nombre, cola, contador):
    contador[nombre] = 0
    while True:
        pedido = cola.get()
        if pedido == "FIN":
            print(f"[{nombre}] Recibí señal de fin. Cerrando cocina.")
            break
        print(f"[{nombre}] Cocinando: {pedido}")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"[{nombre}] Pedido listo: {pedido}")
        contador[nombre] += 1
        print(f"[CONTADOR]-[{nombre}]: {contador[nombre]} pedidos listos")

if __name__ == '__main__':
    cola_pedidos = Queue()
    with Manager() as manager:
        contador_compartido = manager.dict()

        productores = [Process(target=productor, args=(f"Recepcionista-{i+1}", cola_pedidos)) for i in range(2)]
        consumidores = [Process(target=consumidor, args=(f"Cocinero-{i+1}", cola_pedidos, contador_compartido)) for i in range(3)]

        for p in productores: p.start()
        for c in consumidores: c.start()
        for p in productores: p.join()

        for _ in consumidores:
            cola_pedidos.put("FIN")

        for c in consumidores: c.join()

        print("\n📊 RESUMEN FINAL:")
        for cocinero, cantidad in contador_compartido.items():
            print(f"👉 {cocinero} cocinó {cantidad} pedidos.")
