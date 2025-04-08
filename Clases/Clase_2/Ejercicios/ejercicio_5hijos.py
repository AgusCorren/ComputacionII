import os
import time

print(f"Soy el padre, mi PID es {os.getpid()}")

pid = os.fork()
if pid == 0:  # Hijo 1
    print(f"Soy el hijo 1, mi PID es {os.getpid()}, mi padre es {os.getppid()}")
    time.sleep(1)

    pid = os.fork()
    if pid == 0:  # Hijo 2
        print(f"Soy el hijo 2, mi PID es {os.getpid()}, mi padre es {os.getppid()}")
        time.sleep(1)

        pid = os.fork()
        if pid == 0:  # Hijo 3
            print(f"Soy el hijo 3, mi PID es {os.getpid()}, mi padre es {os.getppid()}")
            time.sleep(1)

            pid = os.fork()
            if pid == 0:  # Hijo 4
                print(f"Soy el hijo 4, mi PID es {os.getpid()}, mi padre es {os.getppid()}")
                time.sleep(1)

                pid = os.fork()
                if pid == 0:  # Hijo 5
                    print(f"Soy el hijo 5, mi PID es {os.getpid()}, mi padre es {os.getppid()}")
                    time.sleep(1)