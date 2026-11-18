def sum(n: int) -> int:
    if (n == 1):
        return 1
    else:
        return sum(n - 1) + n

