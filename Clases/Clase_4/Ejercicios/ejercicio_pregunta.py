import os

def main():
    # Creamos dos pipes: uno para cada dirección
    p_to_h_r, p_to_h_w = os.pipe()  # Padre escribe, hijo lee
    h_to_p_r, h_to_p_w = os.pipe()  # Hijo escribe, padre lee

    pid = os.fork()

    if pid == 0:
        # --- Código del Hijo ---
        os.close(p_to_h_w)  # No escribe en el pipe del padre
        os.close(h_to_p_r)  # No lee del pipe al padre

        r = os.fdopen(p_to_h_r, 'r')
        w = os.fdopen(h_to_p_w, 'w')

        pregunta = r.readline().strip()
        print(f"Hijo: recibí la pregunta -> {pregunta}")
        respuesta = f"La respuesta a '{pregunta}' es: 42"

        w.write(respuesta + '\n')
        w.close()
        r.close()
        os._exit(0)

    else:
        # --- Código del Padre ---
        os.close(p_to_h_r)  # No lee del pipe al hijo
        os.close(h_to_p_w)  # No escribe en el pipe del hijo

        w = os.fdopen(p_to_h_w, 'w')
        r = os.fdopen(h_to_p_r, 'r')

        pregunta = "¿Cuál es el sentido de la vida?"
        print(f"Padre: envío la pregunta -> {pregunta}")
        w.write(pregunta + '\n')
        w.close()

        respuesta = r.readline().strip()
        print(f"Padre: el hijo respondió -> {respuesta}")
        r.close()
        os.wait()

if __name__ == '__main__':
    main()