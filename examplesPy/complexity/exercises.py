# snippet: exercise0
def exercise0(n: int):
    for i in range(n):
        for j in range(n):
            print(i)
            print(j)
    for _ in range(n):
        if n > 0:
            print(n)
            exercise0(n - 1)
# snippet: /exercise0

# snippet: exercise1
def exercise1(n: int):
    for i in range(n):
        for j in range(n):
            print(i)
            print(j)
    for _ in range(n):
        if n > 0:
            print(n)
            exercise1(n - 1)
            exercise1(n - 1)
# snippet: /exercise1

# snippet: exercise2
def exercise2(n: int):
    for i in range(n):
        for j in range(n):
            print(i)
            print(j)
            for _ in range(n):
                if n > 0:
                    print(n)
                    exercise2(n - 1)
                    exercise2(n - 1)
# snippet: /exercise2

# snippet: exercise3
def exercise3(n: int):
    for i in range(n):
        for j in range(100):
            print(i)
            print(j)
# snippet: /exercise3

# snippet: exercise4
def exercise4(n: int):
    for i in range(n):
        if n > 0:
            exercise4(n // 2)
# snippet: /exercise4