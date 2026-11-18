def count_to_100_iterative(x: int) -> int:
    while x < 100:
        x = x + 1
        print(x)
    return x

def count_to_100_recursive(x: int) -> int:
    print(x)
    if x < 100:
        return count_to_100_recursive(x + 1)
    else:
        return x

if __name__ == '__main__':
    count_to_100_recursive(90)
    count_to_100_iterative(90)
