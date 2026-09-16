def fak(i: int):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fak(i - 1) * i

if __name__ == '__main__':
    print(fak(2345678))
