if __name__ == '__main__':
    number: int = 7
    while number != 0:
        leastSignificantBit: int = number % 2
        print(leastSignificantBit)
        number = number // 2