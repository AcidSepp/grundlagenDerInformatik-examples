a: int = 42

def funky(b: int) -> int:
    c: int = 43
    while b > 0:
        d = c + b
        b = b - 1
        c = c + d
    return c

def boring(e: int) -> int:
    return e
