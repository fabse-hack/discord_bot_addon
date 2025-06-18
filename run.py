import time

print("hello world")

try:
    print("test")
    time.sleep(5)
    print("Fertig geschlafen!")
except Exception as e:
    print(f"Fehler: {e}")
