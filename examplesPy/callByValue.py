# snippet: callByValue
def add1(a: int):
    a = a + 1

if __name__ == '__main__':
    x: int = 42
    print(x)
    add1(x)
    print(x)
# snippet: /callByValue
