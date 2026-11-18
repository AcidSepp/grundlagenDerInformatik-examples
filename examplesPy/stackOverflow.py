def count_from(n: int):
    print(n)
    if n == 0:
        return
    else:
        count_from(n - 1)

if __name__ == '__main__':
    count_from(1337)