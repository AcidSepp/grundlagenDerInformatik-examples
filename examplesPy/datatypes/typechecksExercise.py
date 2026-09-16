# snippet: functions
def pi() -> float:
    return 3.14

def square(param1: float) -> float:
    return param1 * param1

def equals(param1: float, param2: float) -> bool:
    return param1 == param2

def parse(param1: str) -> float:
    return float(param1)

def convert(param1: float) -> str:
    return str(param1)
# snippet: /functions

# snippet: exercise0
square(pi(), pi())
# snippet: /exercise0

# snippet: exercise1
equals(square(square(square(pi()))), 42.0)
# snippet: /exercise1

# snippet: exercise2
equals(square(123.0), convert("42"))
# snippet: /exercise2

# snippet: exercise3
equals(parse(convert(pi())), square(square(parse("42"))))
# snippet: /exercise3

# snippet: exercise4
a: float = square(parse("42")) + parse("12")
b: str = convert(123) + "Hello"
c: str = convert(a) + b
# snippet: /exercise4