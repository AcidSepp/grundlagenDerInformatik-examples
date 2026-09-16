# snippet: overload
def simple(a: int, b: int):
    print(str(a) + " " + str(b))

def simple(a: int):
    print(str(a))

if __name__ == '__main__':
    simple(42, 43)
    simple(42)
# snippet: /overload
