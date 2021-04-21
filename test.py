import sys
import time


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)


name = 'Pikachu'
print(delay_print(name))