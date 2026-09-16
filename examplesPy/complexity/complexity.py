# snippet: gaussianSum
def gaussianSum(n: int):
    print(n * (n + 1) / 2)
# snippet: /gaussianSum

# snippet: logarithmic
def logarithmic(n: int):
    while n > 2:
        print(n)
        n //= 2
# snippet: /logarithmic

# snippet: linearIterative
def linear_iterative(n: int):
    for _ in range(n):
        print(n)
# snippet: /linearIterative

# snippet: linearRecursive
def linear_recursive(n: int):
    print(n)
    if n > 0:
        linear_recursive(n - 1)
# snippet: /linearRecursive

# snippet: squared
def squared(n: int):
    for i in range(n):
        for j in range(n):
            print("i:" + str(i) + "j: " + str(j))
# snippet: /squared

# snippet: cubic
def cubic(n: int):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print("i:" + str(i) + "j: " + str(j) + "k: " + str(k))
# snippet: /cubic

# snippet: exponential
def exponential(n: int):
    if n > 0:
        print(n)
        exponential(n - 1)
        exponential(n - 1)
# snippet: /exponential

# snippet: sumRule
def sum_rule(n: int):
    for _ in range(n): # P1
        print(n)
    linear_iterative(n) # P2
# snippet: /sumRule

# snippet: multRule
def mult_rule(n: int):
    for _ in range(n): # P1
        linear_iterative(n) # P2
# snippet: /multRule

# snippet: exercise0
def exercise0(n: int):
    cubic(n)
    for _ in range(n):
        exponential(n)
# snippet: /exercise0

# snippet: exercise1
def exercise1(n: int):
    for _ in range(n):
        exponential(n)
        cubic(n)
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                linear_iterative(n)
# snippet: /exercise1

# snippet: exercise2
def exercise2(n: int):
    for _ in range(n):
        cubic(n)
    for _ in range(n):
        for _ in range(n):
            squared(n)
# snippet: /exercise2

# snippet: exercise3
def exercise3(n: int):
    gaussianSum(n)
    logarithmic(n)
    linear_iterative(n)
    cubic(n)
    exponential(n)
# snippet: /exercise3


if __name__ == '__main__':
    logarithmic(67876787)