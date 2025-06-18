import time

print("hello world")

try:
    while True:
        print("test")
        time.sleep(5)
except Exception as e:
    print(f"Fehler: {e}")
