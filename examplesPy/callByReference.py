from typing import List
# snippet: callByReference
def add1(a: List[int]):
    a.append(1)

if __name__ == '__main__':
    x: List[int] = [1,2,3]
    print(x)
    add1(x)
    print(x)
# snippet: /callByReference
