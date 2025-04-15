from multiprocessing import Process, Queue
import time
import random

def recibir_pedidos(cola):
    pedidos = ["Empanadas", "Pizza", "Milanesa", "Hamburguesa", "Lomito"]
    for i in range(5):
        pedido = random.choice(pedidos)
        print(f"[Recepción] Pedido recibido: {pedido}")
        cola.put(pedido)
        time.sleep(random.uniform(0.5, 1.5))

def productor1(cola):
    for _ in range(2):
        pedido = cola.get()
        print(f"[Cocina1] Preparando: {pedido}")
        time.sleep(random.uniform(1, 2))
        print(f"[Cocina1] {pedido} listo!")

def productor2(cola): #Esto lo agregue yo porque GPT me pregunto si podria haber mas de un cocinero, y lo probé y funcionó
    for _ in range(3):
        pedido = cola.get()
        print(f"[Cocina2] Preparando: {pedido}")
        time.sleep(random.uniform(1, 2))
        print(f"[Cocina2] {pedido} listo!")

if __name__ == '__main__':
    cola_pedidos = Queue()

    p1 = Process(target=recibir_pedidos, args=(cola_pedidos,))
    p2 = Process(target=productor1, args=(cola_pedidos,))
    p3 = Process(target=productor2, args=(cola_pedidos,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()