import random
import time

levels = ["INFO", "WARN", "ERROR"]

while True:
    level = levels[random.randint(0, 2)]

    with open("/tmp/var/log/app.log", "a") as logstream:
        logstream.write(f"{level} Pizza Time\n")

    time.sleep(1)
