import time
import sys

NANOS_TO_SECONDS = 1e-9

def is_schalt_jahr_a(year: int) -> bool:
    A = (year % 4) == 0
    B = (year % 100) == 0
    C = (year % 400) == 0
    return A and not (B and not C)

if __name__ == "__main__":
    schalt_jahr_count = 0
    before = time.time_ns()

    for i in range(sys.maxsize):
        if is_schalt_jahr_a(i):
            schalt_jahr_count += 1

    duration = (time.time_ns() - before) * NANOS_TO_SECONDS
    print(f"{schalt_jahr_count} took {duration:.2f} s")
