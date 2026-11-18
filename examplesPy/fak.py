# snippet: recursive
def fak(n: int):
    if n <= 1:
        return 1
    return fak(n - 1) * n
# snippet: /recursive

def fak_iterative(n: int):
    while n <= 1:
        n = (n - 1)

if __name__ == '__main__':
    print(fak(5))
