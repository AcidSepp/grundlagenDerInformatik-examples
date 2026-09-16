# snippet: iterative
def collatz_iterative(x: int) -> int:
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
    return x
# snippet: /iterative

def collatz_recursive(x: int) -> int:
    if x != 1:
        if x % 2 == 0:
            return collatz_recursive(x // 2)
        else:
            return collatz_recursive(x * 3 + 1)
    else:
        return x