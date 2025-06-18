import time
import os

LOG_FILE = "log.txt"
CLEAR_FLAG = "clear.flag"
EXIT_FLAG = "exit.flag"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

def clear_log():
    with open(LOG_FILE, "w") as f:
        f.truncate(0)

def main():
    while True:
        # Logik für Log löschen
        if os.path.exists(CLEAR_FLAG):
            clear_log()
            os.remove(CLEAR_FLAG)
            print("Log gelöscht!")
            log("Log gelöscht!")
        # Logik für Beenden
        if os.path.exists(EXIT_FLAG):
            print("Beende Schleife.")
            log("Beende Schleife.")
            break

        print("hello world")
        log("hello world")
        time.sleep(2)
        print("test")
        log("test")
        time.sleep(1)
        print("Fertig geschlafen!")
        log("Fertig geschlafen!")
        time.sleep(2)

if __name__ == "__main__":
    main()
