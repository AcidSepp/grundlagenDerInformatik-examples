# snippet: def
def my_function(param1: int, param2: bool) -> float:
    if param1 > 0:
        return 0.0
    if param2:
        return 1.0
    return  -1.0
# snippet: /def

# snippet: const
def pi() -> float:
    return 3.14
# snippet: /const

# snippet: oneParam
def square(param1: float) -> float:
    return param1 * param1
# snippet: /oneParam

# snippet: twoParam
def equals(param1: float, param2: float) -> bool:
    return param1 == param2
# snippet: /twoParam

# snippet: correct
square(1337.0)
square(pi())
equals(pi(), square(pi()))
# snippet: /correct

# snippet: incorrect
square(True)
square()
pi(pi())
square(equals(pi(), pi()))
# snippet: /incorrect

# snippet: exercise1
equals(square(square(pi())), square(pi()))
# snippet: /exercise1

# snippet: exercise2
equals(pi(), pi(), pi())
# snippet: /exercise2

# snippet: exercise3
equals(square(square(pi())), square(pi(), pi(pi())))
# snippet: /exercise3