# snippet: recursive
def is_divisible_by_3_recursive(n: int) -> bool:
    if n < 3:
        return n == 0
    else:
        return is_divisible_by_3_recursive(n - 3)
# snippet: /recursive

def is_divisible_by_3_iterative(n: int) -> bool:
    while n >= 3:
        n = n - 3
    return n == 0

# snippet: iterative
def is_divisible_by_5_iterative(n: int) -> bool:
    while n >= 5:
        n = n - 5
    return n == 0
# snippet: /iterative

def is_divisible_by_5_recursive(n: int) -> bool:
    if n < 5:
        return n == 0
    else:
        return is_divisible_by_5_recursive(n - 5)

if __name__ == '__main__':
    print(is_divisible_by_3_recursive(7))
    print(is_divisible_by_3_iterative(7))
    print(is_divisible_by_5_recursive(16))
    print(is_divisible_by_5_iterative(16))