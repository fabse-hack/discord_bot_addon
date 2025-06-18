import time

print("Starte Discord Bot Addon Script...")
while True:
    try:
        print("hello world")
        time.sleep(2)
        print("test")
        time.sleep(1)
        print("Fertig geschlafen!")
        time.sleep(2)
    except Exception as e:
        print(f"Fehler im Hauptloop: {e}")
        time.sleep(5)
